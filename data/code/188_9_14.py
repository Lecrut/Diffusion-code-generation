class ListReverser:
    def reverse(self, iterable):
        return list(reversed(iterable))

if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5]
    reverser = ListReverser()
    reversed_list = reverser.reverse(sample_input)
    print(reversed_list)