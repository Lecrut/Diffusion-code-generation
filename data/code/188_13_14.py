class ListReverser:
    def reverse(self, iterable):
        return iterable[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    sample = [1, 2, 3, 4, 5]
    print(f"Original: {sample}, Reversed: {reverser.reverse(sample)}")