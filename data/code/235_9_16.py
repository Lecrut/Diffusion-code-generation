PATTERN_CONFIG = {'line_length': 7}

def generate_line_pattern(line_length):
    line = '*' * line_length
    return line
if __name__ == '__main__':
    sample_value = PATTERN_CONFIG['line_length']
    pattern = generate_line_pattern(sample_value)
    print(pattern)