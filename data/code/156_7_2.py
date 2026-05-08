def find_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    list3 = []
    list4 = [-1, 5, 10]
    print(f"Average of {list1}: {find_average(list1)}")
    print(f"Average of {list2}: {find_average(list2)}")
    try:
        print(f"Average of {list3}: {find_average(list3)}")
    except ValueError as e:
        print(f"Error for {list3}: {e}")
    print(f"Average of {list4}: {find_average(list4)}")