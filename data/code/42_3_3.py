def build_spaced_string(items, separator):
    result = ""
    for i, item in enumerate(items):
        result += str(item)
        if i < len(items) - 1:
            result += separator
    return result
if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5]
    separator = " "
    output_string = build_spaced_string(input_list, separator)
    print(output_string)