def calculate_total_sum(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(f"Total sum of {sample_list1}: {calculate_total_sum(sample_list1)}")
    
    sample_list2 = [10, -5, 20, 0]
    print(f"Total sum of {sample_list2}: {calculate_total_sum(sample_list2)}")
    
    sample_list3 = []
    print(f"Total sum of {sample_list3}: {calculate_total_sum(sample_list3)}")
    
    sample_list4 = [100]
    print(f"Total sum of {sample_list4}: {calculate_total_sum(sample_list4)}")