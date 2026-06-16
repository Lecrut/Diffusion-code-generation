class ListReverser:
    def __init__(self):
        self._internal_list = []
    def set_list(self, data):
        self._internal_list = list(data)
    def reverse_list(self):
        reversed_list = self._internal_list[::-1]
        self._internal_list = reversed_list
if __name__ == '__main__':
    original_data = [1, 2, 3, 4, 5]
    reverser = ListReverser()
    reverser.set_list(original_data)
    print("Original list before reversal:", original_data)
    reverser.reverse_list()
    print("List after reversal:", original_data)