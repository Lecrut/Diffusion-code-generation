class TupleReverser:
    def reverse(self, input_tuple):
        return input_tuple[::-1]

if __name__ == '__main__':
    reverser = TupleReverser()
    sample_tuple_1 = (1, 2, 3, 4, 5)
    reversed_tuple_1 = reverser.reverse(sample_tuple_1)
    print(reversed_tuple_1)

    sample_tuple_2 = ('a', 'b', 'c', 'd')
    reversed_tuple_2 = reverser.reverse(sample_tuple_2)
    print(reversed_tuple_2)