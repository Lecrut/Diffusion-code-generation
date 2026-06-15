def calculate_average(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return sum(data) / len(data)
if __name__ == '__main__':
    list1 = [10.0, 20.0, 30.0, 40.0]
    list2 = [5.5, 6.5, 7.5]
    empty_list = []
    try:
        avg1 = calculate_average(list1)
        print(f"Average of {list1}: {avg1}")
        avg2 = calculate_average(list2)
        print(f"Average of {list2}: {avg2}")
        calculate_average(empty_list)
    except ValueError as e:
        print(f"Error caught: {e}")