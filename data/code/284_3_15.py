def validate_integer_list(input_list):
    if not all(isinstance(item, int) for item in input_list):
        raise ValueError("All elements must be integers")

def reverse_integer_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    validate_integer_list(sample_list)
    reversed_sample = reverse_integer_list(sample_list)
    print(reversed_sample)