def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return 0
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        return 0

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3, 4, 5],
        [],
        ["a", "b", "c"],
        [10, 20, "error"]
    ]
    
    for values in sample_values:
        print(f"Average of {values}: {calculate_average(values)}")