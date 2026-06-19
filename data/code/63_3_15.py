class ListProcessor:
    def __init__(self, elements):
        self._elements = elements

    def get_first_element(self):
        if not self._elements:
            return None
        return self._elements[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    processor = ListProcessor(sample_list)
    first_element = processor.get_first_element()
    print(first_element)

    empty_list = []
    empty_processor = ListProcessor(empty_list)
    first_empty_element = empty_processor.get_first_element()
    print(first_empty_element)

    single_element_list = [42]
    single_processor = ListProcessor(single_element_list)
    first_single_element = single_processor.get_first_element()
    print(first_single_element)