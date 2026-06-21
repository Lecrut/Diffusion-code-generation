def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers")

def calculate_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 != 0:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    list2 = []
    list3 = [7]

    validate_input(list1)
    print("Median of list1:", calculate_median(list1))

    validate_input(list2)
    print("Median of list2:", calculate_median(list2))

    validate_input(list3)
    print("Median of list3:", calculate_median(list3))