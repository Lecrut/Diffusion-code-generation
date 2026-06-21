def sum_elements(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    result = sum_elements(sample_numbers)
    print(result)