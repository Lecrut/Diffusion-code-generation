def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list1 = [4, 7, 2, 9, 5]
    print(f"Maximum of {sample_list1}: {find_largest_number(sample_list1)}")
    
    sample_list2 = [-3, -8, -1, -6, -2]
    print(f"Maximum of {sample_list2}: {find_largest_number(sample_list2)}")