class ListReverser:
    def reverse(self, iterable):
        return iterable[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    sample1 = [1, 2, 3, 4, 5]
    print(f"Original: {sample1}, Reversed: {reverser.reverse(sample1)}")
    sample2 = ['a', 'b', 'c']
    print(f"Original: {sample2}, Reversed: {reverser.reverse(sample2)}")