class DynamicList:

    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def get_element_by_position(self, position):
        if 0 <= position < len(self.elements):
            return self.elements[position]
        else:
            raise IndexError('Position out of range')
if __name__ == '__main__':
    dynamic_list = DynamicList()
    dynamic_list.add_element('apple')
    dynamic_list.add_element('banana')
    dynamic_list.add_element('cherry')
    try:
        print(dynamic_list.get_element_by_position(1))
    except IndexError as e:
        print(e)