def calculate_average(numbers):
    if not isinstance(numbers, tuple) or not all(isinstance(n, int) for n in numbers):
        raise ValueError("Input must be a non-empty tuple of integers.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    try:
        average = calculate_average(sample_values)
        print(f"Average of {sample_values}: {average}")
    except ValueError as e:
        print(e)

    empty_tuple = ()
    try:
        average = calculate_average(empty_tuple)
        print(f"Average of {empty_tuple}: {average}")
    except ValueError as e:
        print(e)

    mixed_types = (10, 20, '30', 40)
    try:
        average = calculate_average(mixed_types)
        print(f"Average of {mixed_types}: {average}")
    except ValueError as e:
        print(e)