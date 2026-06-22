def mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = mean(sample_data)
    print(result)