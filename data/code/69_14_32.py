def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

def access_elements_by_index(sample_list):
    validate_input(sample_list)
    for index in range(len(sample_list)):
        print(sample_list[index])

if __name__ == '__main__':
    sample_values = [123, 456, 789, 101112, 131415]
    access_elements_by_index(sample_values)