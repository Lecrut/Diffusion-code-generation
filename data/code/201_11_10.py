def calculate_average(numbers):
    if not numbers:
        raise ValueError("The sequence is empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        average = calculate_average(sample_data)
        print(f"The average of {sample_data} is: {average}")
    except ValueError as e:
        print(e)

    sample_data_empty = []
    try:
        average = calculate_average(sample_data_empty)
        print(f"The average of {sample_data_empty} is: {average}")
    except ValueError as e:
        print(e)