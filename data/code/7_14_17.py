def has_special_char_intersection(input_string):
    special_characters = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
    input_chars = set(input_string)
    intersection = input_chars & special_characters
    return len(intersection) > 0

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = has_special_char_intersection(sample_string)
    print(result)