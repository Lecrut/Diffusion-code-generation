def sum_numbers(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    sample1 = [4, 5, 6]
    sample2 = []
    print(sum_numbers(sample1))
    print(sum_numbers(sample2))