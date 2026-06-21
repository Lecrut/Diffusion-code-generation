class ListReverser:

    def reverse_list(self, lst):
        return lst[::-1]
if __name__ == '__main__':
    reverser = ListReverser()
    print(reverser.reverse_list([1, 2, 3, 4]))
    print(reverser.reverse_list(['a', 'b', 'c']))