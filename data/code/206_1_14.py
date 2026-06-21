def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_minimum(sample_list1))
    sample_list2 = [-10, 50, 3, -1]
    print(find_minimum(sample_list2))
    sample_list3 = [42]
    print(find_minimum(sample_list3))