def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = calculate_average(sample_list)
    print(result)