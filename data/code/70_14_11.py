def get_first_last_char(input_string):
    if not input_string:
        return None, None
    first = input_string[0]
    last = input_string[-1]
    return first, last

if __name__ == '__main__':
    sample_input = "Hello, World!"
    first_char, last_char = get_first_last_char(sample_input)
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")