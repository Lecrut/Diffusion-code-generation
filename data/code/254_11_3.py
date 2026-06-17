def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_minimum(sample_list1)
    print(f"The minimum of {sample_list1} is: {result1}")
    sample_list2 = [-10, 0, 5, -20, 3]
    result2 = find_minimum(sample_list2)
    print(f"The minimum of {sample_list2} is: {result2}")
    sample_list3 = [42]
    result3 = find_minimum(sample_list3)
    print(f"The minimum of {sample_list3} is: {result3}")
    sample_list4 = []
    try:
        result4 = find_minimum(sample_list4)
        print(f"The minimum of {sample_list4} is: {result4}")
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")