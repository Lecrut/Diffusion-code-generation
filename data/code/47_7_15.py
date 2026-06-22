def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = mean(sample_list)
    print(result)