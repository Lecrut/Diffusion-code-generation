def generate_pattern(rows, char):
    pattern = ""
    for i in range(rows):
        row = char * (i + 1)
        pattern += row + "\n"
    return pattern.rstrip('\n')
if __name__ == '__main__':
    rows_val = 5
    char_val = '*'
    result = generate_pattern(rows_val, char_val)
    print(result)