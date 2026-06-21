class ListReverser:
    def __init__(self, lst):
        self.lst = lst

    def reverse(self):
        reversed_lst = []
        for item in reversed(self.lst):
            reversed_lst.extend([item])
        return reversed_lst

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(my_list)
    reversed_list = reverser.reverse()
    print(reversed_list)

    another_list = ['a', 'b', 'c', 'd', 'e']
    another_reverser = ListReverser(another_list)
    another_reversed_list = another_reverser.reverse()
    print(another_reversed_list)