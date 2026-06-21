class ListReverser:
    def is_iterable(self, data):
        return hasattr(data, '__iter__')

    def reverse(self, iterable):
        if not self.is_iterable(iterable):
            raise ValueError("Input must be an iterable")
        return list(reversed(iterable))

if __name__ == '__main__':
    reverser = ListReverser()
    sample_input = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse(sample_input)
    print(reversed_list)