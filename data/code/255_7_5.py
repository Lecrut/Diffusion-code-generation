def find_max_float(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample_list = [3.14159, 2.71828, 1.61803, 4.0]
    print(find_max_float(sample_list))
    sample_list_2 = [-5.5, -1.2, -10.0, -0.5]
    print(find_max_float(sample_list_2))
    sample_list_3 = [1.0, 1.0000000000000001, 1.0000000000000002]
    print(find_max_float(sample_list_3))
    empty_list = []
    try:
        find_max_float(empty_list)
    except ValueError as e:
        print(e)