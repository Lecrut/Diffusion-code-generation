CHARACTER_SET = set("0123456789 ")

def contains_only_digits_and_spaces(input_string):
    return all(char in CHARACTER_SET for char in input_string)

if __name__ == '__main__':
    sample_string = "123 456"
    result = contains_only_digits_and_spaces(sample_string)
    print(result)