def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = calculate_average(sample_data)
    print(f"The average of {sample_data} is: {average}")