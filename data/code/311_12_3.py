class ListReverser:
    def __init__(self, data):
        self._internal_list = list(data)
    def reverse_list(self):
        self._internal_list.reverse()
if __name__ == '__main__':
    original_data = [1, 2, 3, 4, 5]
    reverser = ListReverser(original_data)
    print("Original list before reversal:", original_data)
    reverser.reverse_list()
    print("List after reversal:", original_data)