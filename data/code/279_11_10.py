class ListReverser:
    SAMPLE_VALUES = [1, 2, 3, 4, 5]

    @staticmethod
    def reverse_list(numbers):
        return numbers[::-1]

if __name__ == '__main__':
    sample_values = ListReverser.SAMPLE_VALUES
    reversed_values = ListReverser.reverse_list(sample_values)
    print(reversed_values)