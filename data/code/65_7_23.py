class DynamicList:

    def __init__(self):
        self._elements = []

    def add_element(self, element):
        self._elements.append(element)

    def get_element_by_position(self, position):
        if not isinstance(position, int):
            raise TypeError('Position must be an integer')
        if position < 0 or position >= len(self._elements):
            raise IndexError('Position out of range')
        return self._elements[position]
if __name__ == '__main__':
    dynamic_list = DynamicList()
    dynamic_list.add_element('first')
    dynamic_list.add_element('second')
    dynamic_list.add_element('third')
    try:
        print(dynamic_list.get_element_by_position(0))
        print(dynamic_list.get_element_by_position(1))
        print(dynamic_list.get_element_by_position(2))
        print(dynamic_list.get_element_by_position(3))
    except IndexError as e:
        print(f'Caught expected error: {e}')