class ListReverser:
    def __init__(self, data):
        self._data = data
    @staticmethod
    def _swap_elements(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]
    def reverse(self):
        left = 0
        right = len(self._data) - 1
        while left < right:
            self._swap_elements(self._data, left, right)
            left += 1
            right -= 1
        return self._data

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    reverser = ListReverser(sample_list)
    reversed_list = reverser.reverse()
    print(reversed_list)