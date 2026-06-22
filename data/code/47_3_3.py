def compute_average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    total = sum(x for x in numbers)
    count = sum(1 for _ in numbers)
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_average(sample_data)
    print(result)