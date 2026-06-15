def generate_pattern(rows, char):
    pattern = ""
    for i in range(rows):
        pattern += char * (i + 1)
        pattern += "\n"
    return pattern
if __name__ == '__main__':
    rows_val = 5
    char_val = "*"
    result = generate_pattern(rows_val, char_val)
    print(result)