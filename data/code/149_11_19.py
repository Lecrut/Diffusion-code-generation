class StringReverser:
    def __init__(self, data_list):
        self.data_list = data_list

    def reverse_in_place(self):
        self.data_list.reverse()

if __name__ == '__main__':
    my_reverser = StringReverser(["apple", "banana", "cherry"])
    print("Original list:", my_reverser.data_list)
    my_reverser.reverse_in_place()
    print("Reversed list:", my_reverser.data_list)

    another_reverser = StringReverser([1, 2, 3, 4, 5])
    print("Original list:", another_reverser.data_list)
    another_reverser.reverse_in_place()
    print("Reversed list:", another_reverser.data_list)