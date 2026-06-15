def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 15]
    sample_list2 = [7]
    sample_list3 = []
    sample_list4 = [100, 0, 50]
    range1 = calculate_range(sample_list1)
    range2 = calculate_range(sample_list2)
    range3 = calculate_range(sample_list3)
    range4 = calculate_range(sample_list4)
    print(f"Range of {sample_list1}: {range1}")
    print(f"Range of {sample_list2}: {range2}")
    print(f"Range of {sample_list3}: {range3}")
    print(f"Range of {sample_list4}: {range4}")