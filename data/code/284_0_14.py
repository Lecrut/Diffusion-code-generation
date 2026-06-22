class ListReverser:
    @staticmethod
    def reverse(input_list):
        return input_list[::-1]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    reversed_list = ListReverser.reverse(sample)
    print(reversed_list)