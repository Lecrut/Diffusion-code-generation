def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = []
    list3 = [-1, 5, 10, -5]
    try:
        avg1 = calculate_average(list1)
        print(f"Average of {list1}: {avg1}")
        avg3 = calculate_average(list3)
        print(f"Average of {list3}: {avg3}")
        calculate_average(list2)
    except ValueError as e:
        print(f"Error: {e}")