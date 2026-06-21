def contains_zero(numbers):
    if not isinstance(numbers, list):
        raise ValueError('Input must be a list')
    return 0 in numbers
if __name__ == '__main__':
    try:
        sample_list = [10, 20, 30, 40]
        result = contains_zero(sample_list)
        print(result)
        another_sample_list = [-5, -4, 0, 4, 5]
        print(contains_zero(another_sample_list))
        invalid_input = 'not a list'
        print(contains_zero(invalid_input))
    except ValueError as e:
        print(e)