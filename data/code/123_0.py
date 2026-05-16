def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
if __name__ == '__main__':
    sample_numbers = [10, 25, 5, 40, 15]
    result = calculate_sum(sample_numbers)
    print(result)