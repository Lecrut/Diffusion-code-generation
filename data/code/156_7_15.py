def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    test_list_1 = [1, 2, 3, 4, 5]
    test_list_2 = [10, 20, 30]
    test_list_3 = []
    print(f"Average of {test_list_1}: {calculate_average(test_list_1)}")
    print(f"Average of {test_list_2}: {calculate_average(test_list_2)}")
    print(f"Average of {test_list_3}: {calculate_average(test_list_3)}")