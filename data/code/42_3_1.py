def build_spaced_string(input_list):
    result = ""
    for i, element in enumerate(input_list):
        result += str(element)
        if i < len(input_list) - 1:
            result += " "
    return result
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    output_string = build_spaced_string(sample_list)
    print(output_string)