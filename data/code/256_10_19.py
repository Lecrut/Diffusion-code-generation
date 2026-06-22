def calculate_range(numbers):
    if not numbers:
        return 0
    min_val = min(numbers)
    max_val = max(numbers)
    return max_val - min_val

if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 15]
    sample_list2 = [42]
    sample_list3 = []
    sample_list4 = [100, 1, 50]

    print(f"Range of {sample_list1}: {calculate_range(sample_list1)}")
    print(f"Range of {sample_list2}: {calculate_range(sample_list2)}")
    print(f"Range of {sample_list3}: {calculate_range(sample_list3)}")
    print(f"Range of {sample_list4}: {calculate_range(sample_list4)}")