class ListReverser:
    def __init__(self, data):
        self._data = data

    @staticmethod
    def reverse_list_in_place(lst):
        left_index = 0
        right_index = len(lst) - 1
        while left_index < right_index:
            lst[left_index], lst[right_index] = lst[right_index], lst[left_index]
            left_index += 1
            right_index -= 1

    def reverse(self):
        self.reverse_list_in_place(self._data)
        return self._data

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    print(reverser.reverse())