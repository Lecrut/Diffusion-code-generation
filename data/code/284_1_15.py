class TupleReverser:
    @staticmethod
    def reverse(input_tuple):
        return input_tuple[::-1]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    reversed_tuple = TupleReverser.reverse(sample_tuple)
    print(reversed_tuple)