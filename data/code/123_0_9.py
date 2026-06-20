def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers")

def sum_of_elements(lst):
    return sum(lst)

if __name__ == '__main__':
    sample_list = [10, 25, 5, 40, 15]
    validate_input(sample_list)
    result = sum_of_elements(sample_list)
    print(result)