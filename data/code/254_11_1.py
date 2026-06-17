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
    print(f"Minimum of {sample_list1}: {find_minimum(sample_list1)}")
    sample_list2 = [-10, 0, 5, -20, 3]
    print(f"Minimum of {sample_list2}: {find_minimum(sample_list2)}")
    sample_list3 = [42]
    print(f"Minimum of {sample_list3}: {find_minimum(sample_list3)}")
    sample_list4 = []
    try:
        find_minimum(sample_list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")