class TupleReverser:
    def reverse_tuple(self, input_tuple):
        return input_tuple[::-1]

if __name__ == '__main__':
    reverser = TupleReverser()
    sample_tuple = (1, 2, 3, 4, 5)
    reversed_tuple = reverser.reverse_tuple(sample_tuple)
    print(reversed_tuple)