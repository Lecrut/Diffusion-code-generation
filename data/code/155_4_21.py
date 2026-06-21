def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample1 = [7, 8, 9]
    sample2 = []
    result1 = sum_numbers(sample1)
    result2 = sum_numbers(sample2)
    print(result1)
    print(result2)