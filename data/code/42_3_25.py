def build_string_with_spacing(input_list):
    result = ""
    for i, element in enumerate(input_list):
        if i > 0:
            result += " "
        result += str(element)
    return result

if __name__ == '__main__':
    sample_input = ['Hello', 'world', 'this', 'is', 'a', 'test']
    output_string = build_string_with_spacing(sample_input)
    print(output_string)