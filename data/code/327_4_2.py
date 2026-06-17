def calculate_average(numbers: list[float | int]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        average_result = calculate_average(sample_list)
        print(f"The list of numbers is: {sample_list}")
        print(f"The average is: {average_result}")
    except ValueError as e:
        print(f"Error: {e}")
    empty_list = []
    try:
        calculate_average(empty_list)
    except ValueError as e:
        print(f"Testing empty list error: {e}")