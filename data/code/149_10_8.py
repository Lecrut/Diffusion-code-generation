class ListReverser:
    @staticmethod
    def reverse_list(input_list):
        return input_list[::-1]

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    reversed_list = ListReverser.reverse_list(sample_list)
    print(reversed_list)