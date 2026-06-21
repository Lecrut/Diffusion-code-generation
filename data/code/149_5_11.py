class ListReverser:
    @staticmethod
    def reverse(lst):
        return lst[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = ListReverser.reverse(sample_list)
    print(reversed_list)