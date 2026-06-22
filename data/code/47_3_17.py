def compute_average(numbers):
    if not numbers:
        return 0
    return sum(num for num in numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = compute_average(sample_numbers)
    print(result)