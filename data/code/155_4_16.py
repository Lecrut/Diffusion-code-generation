def sum_numbers(numbers):
    if not numbers:
        return 0
    return sum(numbers)
if __name__ == '__main__':
    sample1 = [7, 8, 9]
    sample2 = []
    print(sum_numbers(sample1))
    print(sum_numbers(sample2))