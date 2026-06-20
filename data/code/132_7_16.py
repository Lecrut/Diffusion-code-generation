def is_valid_input(s):
    return s.isalpha()

if __name__ == '__main__':
    sample_values = ["hello", "", "123", "world!", "Python"]
    for value in sample_values:
        result = is_valid_input(value)
        print(f"'{value}': {result}")