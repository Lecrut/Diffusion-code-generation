def calculate_list_sum(numbers):
    if not all((isinstance(num, (int, float)) for num in numbers)):
        raise ValueError('All elements in the list must be numeric.')
    return sum(numbers)
if __name__ == '__main__':
    try:
        list1 = [1, 2, 3, 4, 5]
        result1 = calculate_list_sum(list1)
        print(result1)
        list2 = [10.5, 20.5, 30.0]
        result2 = calculate_list_sum(list2)
        print(result2)
        list3 = [-1, 5, -3, 10]
        result3 = calculate_list_sum(list3)
        print(result3)
        invalid_list = [1, 'two', 3]
        calculate_list_sum(invalid_list)
    except ValueError as e:
        print(e)