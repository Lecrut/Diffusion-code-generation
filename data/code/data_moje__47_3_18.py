def compute_average(numbers):
    if not numbers:
        return 0
    total = sum(number for number in numbers)
    count = sum(1 for _ in numbers)
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = compute_average(sample_list)
    print(result)