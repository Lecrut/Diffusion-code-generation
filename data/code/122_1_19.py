def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    avg = calculate_average(sample_data)
    print(f"Average of {sample_data}: {avg}")