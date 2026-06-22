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
    
    sample_list2 = [-10, 5, 0, -20, 100]
    print(f"Minimum of {sample_list2}: {find_minimum(sample_list2)}")
    
    sample_list3 = [7]
    print(f"Minimum of {sample_list3}: {find_minimum(sample_list3)}")
    
    try:
        find_minimum([])
    except ValueError as e:
        print(e)