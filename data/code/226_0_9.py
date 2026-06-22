class NumberRepeater:
    def __init__(self, numbers):
        self.numbers = numbers

    def repeat_elements(self, repetitions):
        result = []
        for number in self.numbers:
            result.extend([number] * repetitions)
        return result

if __name__ == '__main__':
    repeater = NumberRepeater([1, 2, 3, 4, 5])
    repeated_sequence = repeater.repeat_elements(10)
    print(repeated_sequence)