def get_first_last_chars(input_string):
    first_char = input_string[0]
    last_char = input_string[-1]
    return first_char, last_char

if __name__ == '__main__':
    sample_string = "Hello, World!"
    first_char, last_char = get_first_last_chars(sample_string)
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")