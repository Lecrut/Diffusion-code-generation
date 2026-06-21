class CommonElementsFinder:
    def __init__(self, iterable1, iterable2):
        self.iterable1 = iter(iterable1)
        self.iterable2 = iter(iterable2)

    def _is_in_other(self, item, other_iterable):
        for element in other_iterable:
            if element == item:
                return True
            elif element > item:
                break
        return False

    def find_common_elements(self):
        return (item for item in self.iterable1 if self._is_in_other(item, self.iterable2))

if __name__ == '__main__':
    finder = CommonElementsFinder([1, 5, 2, 8, 3, 9, 4, 7], [8, 3, 1, 9, 6, 2, 10, 5])
    common_elements = list(finder.find_common_elements())
    print(common_elements)