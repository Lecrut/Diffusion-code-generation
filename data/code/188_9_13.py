class ListReverser:
    def reverse(self, iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError("Input is not an iterable")
        return list(reversed(iterable))

if __name__ == '__main__':
    reverser = ListReverser()
    sample_input = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse(sample_input)
    print(reversed_list)