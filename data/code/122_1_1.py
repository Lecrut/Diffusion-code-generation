def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = [10, 20, 30]
    try:
        avg1 = calculate_average(list1)
        print(f"Average of {list1}: {avg1}")
    except ValueError as e:
        print(f"Error for list1: {e}")
    try:
        avg2 = calculate_average(list2)
        print(f"Average of {list2}: {avg2}")
    except ValueError as e:
        print(f"Error for list2: {e}")
    try:
        avg3 = calculate_average(list3)
        print(f"Average of {list3}: {avg3}")
    except ValueError as e:
        print(f"Error for list3: {e}")