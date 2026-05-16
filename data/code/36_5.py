def reverse_string_generator(input_string):
    for char in reversed(input_string):
        yield char
if __name__ == '__main__':
    sample_string = "Hello World"
    reversed_chars = reverse_string_generator(sample_string)
    result_list = list(reversed_chars)
    print(result_list)
    large_string = "This is a very large string for testing memory efficiency" * 10000
    reversed_large_string = reverse_string_generator(large_string)
    print("--- Large String Test ---")
    print(list(reversed_large_string)[:10])
    print("...")
    print(list(reversed_large_string)[-10:])