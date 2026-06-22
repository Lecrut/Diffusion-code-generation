class ArrayExtender:
    def __init__(self):
        self.sequence = [1, 2, 3]

    def extend_sequence(self, num_repeats):
        extended_sequence = (self.sequence * num_repeats)[:len(self.sequence)]
        return extended_sequence

if __name__ == '__main__':
    extender = ArrayExtender()
    result = extender.extend_sequence(5)
    print(result)