class ListReverser:
    def __init__(self, data):
        self._internal_list = list(data)
    def reverse_list(self):
        reversed_list = self._internal_list[::-1]
        self._internal_list = reversed_list
if __name__ == '__main__':
    original_data = [1, 2, 3, 4, 5]
    reverser = ListReverser(original_data)
    print("Original data before reversal:", original_data)
    reverser.reverse_list()
    print("Data after reversal:", original_data)
    original_data_2 = ['a', 'b', 'c', 'd']
    reverser_2 = ListReverser(original_data_2)
    print("\nOriginal data 2 before reversal:", original_data_2)
    reverser_2.reverse_list()
    print("Data 2 after reversal:", original_data_2)