def build_spaced_string(input_list):
    spaced_elements = []
    for element in input_list:
        spaced_elements.append(str(element))
    return ' '.join(spaced_elements)

if __name__ == '__main__':
    sample_values = ["dog", "cat", "elephant", "giraffe"]
    result_string = build_spaced_string(sample_values)
    print(result_string)