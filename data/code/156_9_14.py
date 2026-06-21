def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

if __name__ == '__main__':
    sample_list1 = [5, 15, 25, 35, 45]
    sample_list2 = []
    sample_list3 = [10.5, 20.5, 30.5]

    print(f"Average of {sample_list1}: {calculate_average(sample_list1)}")
    print(f"Average of {sample_list2}: {calculate_average(sample_list2)}")
    print(f"Average of {sample_list3}: {calculate_average(sample_list3)}")