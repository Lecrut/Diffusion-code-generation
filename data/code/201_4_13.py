def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    average_result = calculate_average(sample_list)
    print(f"Average of {sample_list}: {average_result}")