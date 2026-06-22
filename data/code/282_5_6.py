MAX_SEQUENCE_LENGTH = 1000

def sum_sequence(numbers):
    if len(numbers) > MAX_SEQUENCE_LENGTH:
        raise ValueError("Sequence too long")
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = sum_sequence(sample_numbers)
    print(result)