class ListReverser:
    @staticmethod
    def reverse_using_iter(input_list):
        return list(reversed(input_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = ListReverser.reverse_using_iter(sample_list)
    print(reversed_list)