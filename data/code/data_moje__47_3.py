def compute_average(numbers):
    if not numbers:
        return 0.0
    total = sum(x for x in numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = compute_average(sample_values)
    print(result)