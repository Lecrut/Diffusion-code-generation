def calculate_mean(numbers):
    if not numbers:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_numbers)
    print(f"The mean of the numbers is: {result}")