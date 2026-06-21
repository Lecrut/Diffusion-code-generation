def get_middle_value(numbers):
    numbers.sort()
    length = len(numbers)
    middle_index = length // 2
    if length % 2 == 0:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2
    else:
        return numbers[middle_index]

if __name__ == '__main__':
    sample_list1 = [7, 3, 5, 9]
    print("Middle value of", sample_list1, "is:", get_middle_value(sample_list1))
    
    sample_list2 = [8, 6, 4, 2, 0]
    print("Middle value of", sample_list2, "is:", get_middle_value(sample_list2))