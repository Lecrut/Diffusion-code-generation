def avg(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48, 60]
    print(avg(sample_values))