class ListReverser:
    def reverse(self, iterable):
        reversed_list = []
        for item in iterable:
            reversed_list.insert(0, item)
        return reversed_list

if __name__ == '__main__':
    reverser = ListReverser()
    sample_input = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse(sample_input)
    print(reversed_list)