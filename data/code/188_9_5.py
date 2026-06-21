class ListReverser:
    def reverse(self, iterable):
        return list(reversed(iterable))

if __name__ == '__main__':
    reverser = ListReverser()
    sample_input = ['x', 'y', 'z']
    reversed_list = reverser.reverse(sample_input)
    print(f"Original: {sample_input}, Reversed: {reversed_list}")