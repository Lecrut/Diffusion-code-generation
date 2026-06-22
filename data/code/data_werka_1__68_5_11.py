def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    if len(data) < 2:
        raise ValueError("List must contain at least two elements.")

def absolute_differences(data):
    validate_input(data)
    for i in range(len(data) - 1):
        yield abs(data[i+1] - data[i])

if __name__ == '__main__':
    sample_list = [10, 3, 7, 2, 5]
    differences_generator = absolute_differences(sample_list)
    result_list = list(differences_generator)
    print(result_list)