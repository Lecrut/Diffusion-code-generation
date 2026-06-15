def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    list3 = []
    list4 = [-10, 20, 30]
    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    print(f"Average of {list3}: {calculate_average(list3)}")
    print(f"Average of {list4}: {calculate_average(list4)}")