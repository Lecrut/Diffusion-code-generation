def extract_first_alpha(s):
    for char in s:
        if char.isalpha():
            return char
    return None
if __name__ == '__main__':
    sample_string = '123abc456'
    result = extract_first_alpha(sample_string)
    print(result)