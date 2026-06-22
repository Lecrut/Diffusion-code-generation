def sum_sequence_with_generator(numbers):
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = sum_sequence_with_generator(sample_numbers)
    print(result)