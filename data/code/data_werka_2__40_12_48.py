def first_alphabetic_char(s):
    for char in s:
        if char.isalpha():
            return char
    raise ValueError("No alphabetic character found")

if __name__ == '__main__':
    sample_string = "123abc456"
    result = first_alphabetic_char(sample_string)
    print(result)