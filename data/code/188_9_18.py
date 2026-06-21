class ListReverser:
    def reverse(self, iterable):
        return list(reversed(iterable))

if __name__ == '__main__':
    reverser = ListReverser()
    result = reverser.reverse([1, 2, 3, 4, 5])
    print(result)