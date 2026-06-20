def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average_value = calculate_average(sample_data)
    print(f"Average of {sample_data}: {average_value}")