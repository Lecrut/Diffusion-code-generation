class ArrayExtender:
    SEQUENCE = [1, 2, 3]

    @staticmethod
    def extend_and_print(sequence, num_repeats):
        full_sequence = sequence * num_repeats
        print(full_sequence)

if __name__ == '__main__':
    extender = ArrayExtender()
    extender.extend_and_print(ArrayExtender.SEQUENCE, 5)