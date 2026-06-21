class ListReverser:
    def reverse(self, iterable):
        return list(reversed(iterable))

if __name__ == '__main__':
    reverser = ListReverser()
    sample_input = [10, 20, 30, 40, 50]
    reversed_list = reverser.reverse(sample_input)
    print(f"Original: {sample_input}, Reversed: {reversed_list}")