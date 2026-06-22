def validate_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary.")
    if len(input_dict) == 0:
        raise ValueError("Dictionary cannot be empty.")

def calculate_difference_of_extremes(input_dict):
    validate_dict(input_dict)
    return max(input_dict.values()) - min(input_dict.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5}
    result = calculate_difference_of_extremes(sample_dict)
    print(f"Difference between max and min values: {result}")