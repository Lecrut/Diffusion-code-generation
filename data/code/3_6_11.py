def remove_vowels(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    vowels = frozenset('aeiouAEIOU')
    filtered_chars = filter(lambda char: char not in vowels, input_string)
    return "".join(filtered_chars)

if __name__ == '__main__':
    test_data = "Hello World"
    output = remove_vowels(test_data)
    print(output)