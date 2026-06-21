class ListReverser:
    def reverse(self, iterable):
        return list(reversed(iterable))

if __name__ == '__main__':
    reverser = ListReverser()
    sample_input1 = [1, 2, 3, 4, 5]
    sample_input2 = ['a', 'b', 'c']
    sample_input3 = []
    print(f"Reversed {sample_input1}: {reverser.reverse(sample_input1)}")
    print(f"Reversed {sample_input2}: {reverser.reverse(sample_input2)}")
    print(f"Reversed {sample_input3}: {reverser.reverse(sample_input3)}")