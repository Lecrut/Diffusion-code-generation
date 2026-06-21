class ListReverser:
    def __init__(self):
        self.data = []

    def set_data(self, data_list):
        self.data = data_list

    def reverse_in_place(self):
        self.data.reverse()

if __name__ == '__main__':
    reverser1 = ListReverser()
    reverser1.set_data([1, 2, 3, 4, 5])
    print("Original list:", reverser1.data)
    reverser1.reverse_in_place()
    print("Reversed list:", reverser1.data)

    reverser2 = ListReverser()
    reverser2.set_data(['a', 'b', 'c', 'd'])
    print("Original list:", reverser2.data)
    reverser2.reverse_in_place()
    print("Reversed list:", reverser2.data)