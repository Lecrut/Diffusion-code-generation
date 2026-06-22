class TupleReverser:
    @staticmethod
    def reverse(input_tuple):
        return input_tuple[::-1]

if __name__ == '__main__':
    reverser = TupleReverser()
    sample_tuple = (1, 2, 3, 4, 5)
    reversed_tuple = reverser.reverse(sample_tuple)
    print(reversed_tuple)

    sample_tuple_2 = ('a', 'b', 'c', 'd')
    reversed_tuple_2 = reverser.reverse(sample_tuple_2)
    print(reversed_tuple_2)