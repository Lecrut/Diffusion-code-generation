class ListReverser:
    def reverse_list(self, input_list):
        return list(reversed(input_list))

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list}")
    reversed_list = reverser.reverse_list(sample_list)
    print(f"Reversed list: {reversed_list}")