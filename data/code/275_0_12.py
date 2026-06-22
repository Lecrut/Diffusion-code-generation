def transform_strings(string_list):
    transformed_list = []
    for item in string_list:
        transformed_list.append(item.upper())
    return transformed_list

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry"]
    output = transform_strings(sample_data)
    for line in output:
        print(line)