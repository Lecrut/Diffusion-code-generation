class ListProcessor:

    def __init__(self, elements):
        self.elements = elements

    def pop_element(self, index):
        try:
            return self.elements.pop(index)
        except IndexError:
            raise ValueError('Index out of range')
if __name__ == '__main__':
    INITIAL_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_POP = 2
    processor = ListProcessor(INITIAL_LIST)
    try:
        popped_element = processor.pop_element(INDEX_TO_POP)
        print(f'Popped element: {popped_element}')
        print(f'List after popping: {processor.elements}')
        additional_popped_element = processor.pop_element(0)
        print(f'Additional popped element: {additional_popped_element}')
        print(f'List after additional popping: {processor.elements}')
    except ValueError as e:
        print(e)