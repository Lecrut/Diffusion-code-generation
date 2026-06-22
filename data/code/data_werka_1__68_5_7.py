def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the list must be numbers.")

def absolute_differences(data):
    validate_input(data)
    return (abs(data[i+1] - data[i]) for i in range(len(data) - 1))

if __name__ == '__main__':
    sample_list = [7, 3, 9, 2, 5]
    differences = list(absolute_differences(sample_list))
    print(differences)