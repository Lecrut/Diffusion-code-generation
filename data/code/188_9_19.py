class ListReverser:
    def reverse(self, iterable):
        try:
            return list(reversed(iterable))
        except TypeError as e:
            raise ValueError("Input must be an iterable") from e

if __name__ == '__main__':
    reverser = ListReverser()
    sample_input = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse(sample_input)
    print(reversed_list)