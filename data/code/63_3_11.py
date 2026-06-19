class ElementFinder:
    def __init__(self, elements):
        self._items = elements

    def fetch_first(self):
        return None if not self._items else self._items[0]

if __name__ == '__main__':
    sample_elements = [1, 2, 3, 4]
    element_finder = ElementFinder(sample_elements)
    first_element = element_finder.fetch_first()
    print(first_element)

    empty_elements = []
    empty_finder = ElementFinder(empty_elements)
    first_empty = empty_finder.fetch_first()
    print(first_empty)