def sum_mixed_numbers(numbers):
    return sum(float(num) for num in numbers)

if __name__ == '__main__':
    sample_values = [3, 4.5, 2, 6.7]
    print(sum_mixed_numbers(sample_values))