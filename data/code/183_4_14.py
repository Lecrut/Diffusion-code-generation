def strip_newlines(name):
    return name.strip()

def convert_names_to_list(names_str):
    lines = names_str.split('\n')
    valid_lines = [strip_newline(line) for line in lines if line]
    return valid_lines

if __name__ == '__main__':
    sample_names = "Alice\nBob\nCharlie"
    print(convert_names_to_list(sample_names))