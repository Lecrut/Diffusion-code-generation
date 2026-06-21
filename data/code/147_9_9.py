def validate_input(input_list):
    if not isinstance(input_list, list) or not all(isinstance(item, (int, float)) for item in input_list):
        raise ValueError("Input must be a list of numbers")

def sort_numbers(number_list):
    return sorted(number_list)

if __name__ == '__main__':
    sample_list = [3.5, 1, 2.5, -0.5, 0]
    validate_input(sample_list)
    sorted_list = sort_numbers(sample_list)
    print(sorted_list)