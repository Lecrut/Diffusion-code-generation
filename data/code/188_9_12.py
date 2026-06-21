class ListReverser:
    def reverse(self, iterable):
        return list(reversed(iterable))

if __name__ == '__main__':
    reverser = ListReverser()
    sample1 = [1, 2, 3, 4, 5]
    sample2 = []
    sample3 = [7]
    sample4 = ['a', 'b', 'c']
    sample5 = [99]

    print(f"Reversing {sample1}: {reverser.reverse(sample1)}")
    print(f"Reversing {sample2}: {reverser.reverse(sample2)}")
    print(f"Reversing {sample3}: {reverser.reverse(sample3)}")
    print(f"Reversing {sample4}: {reverser.reverse(sample4)}")
    print(f"Reversing {sample5}: {reverser.reverse(sample5)}")