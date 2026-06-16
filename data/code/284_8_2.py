class ListReverser:
    def __init__(self):
        self._internal_list = []
    def set_list(self, data):
        self._internal_list = list(data)
    def reverse_and_return(self):
        self._internal_list.reverse()
        return self._internal_list
if __name__ == '__main__':
    reverser = ListReverser()
    sample_data = [1, 2, 3, 4, 5]
    reverser.set_list(sample_data)
    reversed_list = reverser.reverse_and_return()
    print(reversed_list)