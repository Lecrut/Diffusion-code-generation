class CommonElementsFinder:
    def __init__(self, iterable1, iterable2):
        self.iterable1 = iter(iterable1)
        self.iterable2 = iter(iterable2)

    def _find_next_common(self):
        seen_in_first = set()
        while True:
            try:
                item = next(self.iterable1)
                seen_in_first.add(item)
            except StopIteration:
                break
        for item in self.iterable2:
            if item in seen_in_first:
                yield item

    def get_common_elements(self):
        return list(self._find_next_common())

if __name__ == '__main__':
    finder = CommonElementsFinder([1, 5, 2, 8, 3, 9, 4, 7], [8, 3, 1, 9, 6, 2, 10, 5])
    common_elements = finder.get_common_elements()
    print(common_elements)