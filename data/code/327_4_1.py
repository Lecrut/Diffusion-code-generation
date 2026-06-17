def calculate_average(numbers: list[float | int]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        result = calculate_average(sample_list)
        print(f"The list is: {sample_list}")
        print(f"The average is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_list_two = [2.5, 3.5, 1.0]
    try:
        result_two = calculate_average(sample_list_two)
        print(f"\nThe list is: {sample_list_two}")
        print(f"The average is: {result_two}")
    except ValueError as e:
        print(f"Error: {e}")