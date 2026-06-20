def print_chars_at_positions(s, positions):
    for pos in positions:
        if 0 <= pos < len(s):
            print(s[pos])

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_positions = [0, 7, 12]
    print_chars_at_positions(sample_string, sample_positions)