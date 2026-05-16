def build_spaced_string(input_list):
    result = ""
    for i, element in enumerate(input_list):
        result += str(element)
        if i < len(input_list) - 1:
            result += " "
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    output = build_spaced_string(sample_list)
    print(output)