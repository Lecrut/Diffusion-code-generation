def mean(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10.0, 20.0, 30.0, 40.0, 50.0]
    result = mean(sample_values)
    print(result)
    empty_result = mean([])
    print(empty_result)