class ListReverser:
    @staticmethod
    def reverse_list(input_list):
        return list(reversed(input_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list}")
    reversed_list = ListReverser.reverse_list(sample_list)
    print(f"Reversed list: {reversed_list}")