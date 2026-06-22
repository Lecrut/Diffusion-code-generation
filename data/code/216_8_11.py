def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 != 0:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    sample_values = [
        ([3, 1, 2, 4, 5], 3),
        ([10, 20, 30, 40, 50], 30),
        ([1, 2, 3, 4, 5, 6], 3.5),
        ([7], 7)
    ]
    for values, expected in sample_values:
        try:
            result = calculate_median(values)
            print(f"Input {values}: Median {result} == Expected {expected}")
        except ValueError as e:
            print(e)