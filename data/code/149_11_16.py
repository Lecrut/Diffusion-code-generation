class StringReverser:
    def __init__(self):
        self.data_list = []

    def set_data(self, data_list):
        self.data_list = data_list

    def reverse_in_place(self):
        self.data_list.reverse()

if __name__ == '__main__':
    reverser = StringReverser()
    sample_strings = ["apple", "banana", "cherry"]
    print("Original list:", sample_strings)
    reverser.set_data(sample_strings)
    reverser.reverse_in_place()
    print("Reversed list:", sample_strings)