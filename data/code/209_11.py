def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    try:
        avg1 = calculate_average(list1)
        print(f"Average of {list1}: {avg1}")
        avg2 = calculate_average(list2)
        print(f"Average of {list2}: {avg2}")
        calculate_average(empty_list)
    except ValueError as e:
        print(f"Error caught: {e}")