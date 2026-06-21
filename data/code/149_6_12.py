class ListReverser:
    def reverse(self, lst):
        reversed_lst = []
        for item in reversed(lst):
            reversed_lst.extend([item])
        return reversed_lst

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse(sample_list)
    print(reversed_list)