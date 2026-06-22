def find_maximum(numbers):
    if not numbers:
        return float('-inf')
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 3]
    print(f"Maximum of {sample_list1}: {find_maximum(sample_list1)}")
    
    sample_list2 = [-10, -5, -20, -1]
    print(f"Maximum of {sample_list2}: {find_maximum(sample_list2)}")