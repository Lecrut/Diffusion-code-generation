def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    if len(data) < 2:
        raise ValueError("List must contain at least two elements")

def absolute_differences(data):
    validate_input(data)
    for i in range(1, len(data)):
        yield abs(data[i] - data[i - 1])

if __name__ == '__main__':
    sample_list = [10, 3, 7, 5, 9]
    differences_generator = absolute_differences(sample_list)
    result_list = list(differences_generator)
    print(result_list)