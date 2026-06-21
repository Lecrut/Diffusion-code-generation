def calculate_total_sum(numbers: list) -> int:
    return sum(numbers)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [10, -5, 20, 0]
    sample_list3 = []
    sample_list4 = [100]

    print(f"Sum of {sample_list1}: {calculate_total_sum(sample_list1)}")
    print(f"Sum of {sample_list2}: {calculate_total_sum(sample_list2)}")
    print(f"Sum of {sample_list3}: {calculate_total_sum(sample_list3)}")
    print(f"Sum of {sample_list4}: {calculate_total_sum(sample_list4)}")