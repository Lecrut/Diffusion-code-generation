def rle(input_string):
    if not input_string:
        return []
    result = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    test_string = "aaabbcdddd"
    output = rle(test_string)
    print(output)