def validate_input(line):
    if not isinstance(line, str) or ';' not in line:
        raise ValueError("Input must be a string containing semicolons")

def parse_names(line):
    validate_input(line)
    return [name.strip() for name in line.split(';') if name.strip()]

if __name__ == '__main__':
    sample_line = "Alice; Bob ; Charlie;; David"
    print(parse_names(sample_line))