def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(f"The average of {sample_numbers} is: {calculate_average(sample_numbers)}")