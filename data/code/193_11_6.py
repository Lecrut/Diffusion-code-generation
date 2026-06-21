def calculate_total(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(f"Total of {sample_list1}: {calculate_total(sample_list1)}")
    
    sample_list2 = [10, -5, 20, 0]
    print(f"Total of {sample_list2}: {calculate_total(sample_list2)}")
    
    empty_list = []
    print(f"Total of {empty_list}: {calculate_total(empty_list)}")