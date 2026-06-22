def sum_sequence(numbers):
    if not numbers:
        return 0
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(sum_sequence(sample_numbers))