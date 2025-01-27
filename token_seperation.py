import re

# Define token categories
keywords = ["if", "else", "while", "for", "return", "int", "float", "char", "double", "void"]
operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=', '&&', '||', '%']
special_characters = [';', ',', '(', ')', '{', '}']

def categorize_token(token):
    if token in keywords:
        return f"{token} - Keyword"
    elif token in operators:
        return f"{token} - Operator"
    elif token in special_characters:
        return f"{token} - Special Character"
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):  # Identifier pattern
        return f"{token} - Identifier"
    elif re.match(r'^\d+(\.\d+)?$', token):  # Number pattern (integer or float)
        return f"{token} - Constant"
    else:
        return f"{token} - Unknown"

def tokenize_line(line):
    # Split the line into tokens using regex
    tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|[-+*/%=<>!]+|\d+\.\d+|\d+|[;(),{}]', line)
    return tokens

def main():
    input_file = "input.txt"
    print("\nTOKEN SEPARATION\n")
    try:
        with open(input_file, "r") as file:
            for line_no, line in enumerate(file, start=1):
                print(f"Line {line_no}: {line.strip()}")
                tokens = tokenize_line(line)
                for token in tokens:
                    print(categorize_token(token))
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")

if __name__ == "__main__":
    main()
