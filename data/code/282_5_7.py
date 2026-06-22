def sum_sequence(numbers):
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = sum_sequence(sample_numbers)
    print(result)