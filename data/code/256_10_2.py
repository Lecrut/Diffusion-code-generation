def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 15]
    result1 = calculate_range(sample_list1)
    print(f"The range of {sample_list1} is: {result1}")
    sample_list2 = [42]
    result2 = calculate_range(sample_list2)
    print(f"The range of {sample_list2} is: {result2}")
    sample_list3 = []
    result3 = calculate_range(sample_list3)
    print(f"The range of {sample_list3} is: {result3}")
    sample_list4 = [100, 50, 25]
    result4 = calculate_range(sample_list4)
    print(f"The range of {sample_list4} is: {result4}")