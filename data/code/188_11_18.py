class ListReverser:
    def __init__(self, initial_list):
        self.list = initial_list

    def reverse(self):
        self.list.reverse()

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    print('Original list:', reverser.list)
    reverser.reverse()
    print('Reversed list:', reverser.list)