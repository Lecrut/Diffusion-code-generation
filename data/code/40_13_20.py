def first_alphabetic_character(s):
    for char in s:
        if char.isalpha():
            return char
    return None
if __name__ == '__main__':
    sample_string = '123abc456'
    result = first_alphabetic_character(sample_string)
    print(result)