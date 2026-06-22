class TupleReverser:
    def __init__(self, input_tuple):
        self.input_tuple = input_tuple

    def reverse(self):
        return self.input_tuple[::-1]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    reverser = TupleReverser(sample_tuple)
    reversed_tuple = reverser.reverse()
    print(reversed_tuple)

    another_sample_tuple = ('a', 'b', 'c', 'd')
    another_reverser = TupleReverser(another_sample_tuple)
    another_reversed_tuple = another_reverser.reverse()
    print(another_reversed_tuple)