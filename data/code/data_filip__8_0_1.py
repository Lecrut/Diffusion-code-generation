def split_commas(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    result = []
    start = 0
    length = len(input_string)
    while start < length:
        comma_index = input_string.find(',', start)
        if comma_index == -1:
            substring = input_string[start:]
            if substring:
                result.append(substring)
            break
        substring = input_string[start:comma_index]
        if substring:
            result.append(substring)
        start = comma_index + 1
    return result

if __name__ == '__main__':
    test_data = "apple,banana,,cherry,  ,date,"
    print(split_commas(test_data))