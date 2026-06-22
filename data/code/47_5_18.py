def mean(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    values = [10, 20, 30, 40, 50]
    result = mean(values)
    print(result)