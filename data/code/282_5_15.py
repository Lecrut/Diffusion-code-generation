class SequenceSum:
    @staticmethod
    def sum_sequence(numbers):
        return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = SequenceSum.sum_sequence(sample_numbers)
    print(result)