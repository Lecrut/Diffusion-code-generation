class NumberRepeater:
    REPEAT_COUNT = 10

    @staticmethod
    def repeat_elements(sequence):
        result = []
        for element in sequence:
            result.extend([element] * NumberRepeater.REPEAT_COUNT)
        return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    repeater = NumberRepeater()
    output = repeater.repeat_elements(sample_sequence)
    print(output)