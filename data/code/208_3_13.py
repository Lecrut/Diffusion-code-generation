def calculate_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = calculate_mean(sample_numbers)
    print(f"The mean of the numbers is: {result}")