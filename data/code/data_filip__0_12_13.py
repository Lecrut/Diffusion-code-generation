def extract_digits(input_string):
    return [char for char in input_string if char.isdigit()]

if __name__ == '__main__':
    sample = "a1b2c3!@# 4$ 5% 6^ 7& 8* 9( 0) + = - _ "
    result = extract_digits(sample)
    print(result)