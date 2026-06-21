def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3, 4, 5],
        [],
        ["a", "b", "c"],
        [10, 20, "error"]
    ]
    
    for values in sample_values:
        average = calculate_average(values)
        print(f"Average of {values}: {average}")