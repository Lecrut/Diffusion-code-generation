class ListReverser:
    @staticmethod
    def reverse(lst):
        reversed_lst = []
        for item in reversed(lst):
            reversed_lst.extend([item])
        return reversed_lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = ListReverser.reverse(sample_list)
    print(reversed_list)