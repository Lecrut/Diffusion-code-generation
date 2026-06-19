def build_spaced_string(input_list):
    if not input_list:
        return ""
    
    spaced_elements = (str(element) for element in input_list)
    result = " ".join(spaced_elements)
    return result

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    output = build_spaced_string(sample_list)
    print(output)