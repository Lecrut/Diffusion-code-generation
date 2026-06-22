class ListReverser:
    def __init__(self, list1, list2):
        self.list1 = list1[::-1]
        self.list2 = list2[::-1]

if __name__ == '__main__':
    reverser = ListReverser([1, 2, 3], [4, 5, 6])
    print("First list reversed:", reverser.list1)
    print("Second list reversed:", reverser.list2)