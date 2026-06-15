def generate_pattern(rows: int, char: str) -> str:
    pattern = ""
    for _ in range(rows):
        pattern += char * (len(pattern) + 1)
    return pattern
if __name__ == '__main__':
    rows_val = 5
    char_val = '#'
    result = generate_pattern(rows_val, char_val)
    print(result)