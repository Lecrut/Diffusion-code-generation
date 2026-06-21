def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    empty_list = []
    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    print(f"Average of {empty_list}: {calculate_average(empty_list)}")