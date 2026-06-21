class ListReverser:
    def __init__(self, lst):
        self.lst = lst

    def reverse(self):
        reversed_lst = []
        for item in reversed(self.lst):
            reversed_lst.extend([item])
        return reversed_lst

if __name__ == '__main__':
    reverser = ListReverser([1, 2, 3, 4, 5])
    print(reverser.reverse())