def find_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    empty_list = []
    try:
        avg1 = find_average(list1)
        print(f"The average of {list1} is: {avg1}")
        avg2 = find_average(list2)
        print(f"The average of {list2} is: {avg2}")
        find_average(empty_list)
    except ValueError as e:
        print(f"Error: {e}")