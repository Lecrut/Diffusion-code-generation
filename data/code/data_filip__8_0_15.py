def split_commas(input_string):
    parts = input_string.split(',')
    result = []
    for part in parts:
        if part:
            result.append(part)
    return result

if __name__ == '__main__':
    test_string = "apple,banana,,cherry,,"
    output = split_commas(test_string)
    print(output)