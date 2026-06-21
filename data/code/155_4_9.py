def sum_numbers(numbers):
    return sum(numbers) if numbers else 0
if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = []
    print(sum_numbers(sample1))
    print(sum_numbers(sample2))