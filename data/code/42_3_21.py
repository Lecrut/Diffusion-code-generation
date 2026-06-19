def build_spaced_string(input_list):
    result = []
    for element in input_list:
        result.append(str(element))
    return " ".join(result)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    output = build_spaced_string(sample_list)
    print(output)