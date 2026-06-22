def compute_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)