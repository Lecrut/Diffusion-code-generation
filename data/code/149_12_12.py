class ListReverser:
    @staticmethod
    def reverse_list(numbers):
        return list(reversed(numbers))

if __name__ == '__main__':
    sample_input = [1, 5, 3, 9, 2]
    reversed_list = ListReverser.reverse_list(sample_input)
    print(reversed_list)