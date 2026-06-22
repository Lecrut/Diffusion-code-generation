MIN_LENGTH = 2

def validate_list_and_get_penultimate(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) < MIN_LENGTH:
        raise ValueError("List must contain at least two elements")
    return retrieve_second_to_last(data)

def retrieve_second_to_last(sequence):
    index = len(sequence) - 2
    return sequence[index]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    result = validate_list_and_get_penultimate(sample_data)
    print(result)
    try:
        validate_list_and_get_penultimate("not a list")
    except TypeError:
        print("Error: Input must be a list")
    try:
        validate_list_and_get_penultimate([1])
    except ValueError:
        print("Error: List must contain at least two elements")