def validate_list(input_data):
    if not isinstance(input_data, list):
        raise ValueError("Input must be a list")

def access_elements_by_index(sample_list):
    validate_list(sample_list)
    for index in range(len(sample_list)):
        print(sample_list[index])

if __name__ == '__main__':
    sample_values = [7, 17, 27, 37, 47]
    access_elements_by_index(sample_values)