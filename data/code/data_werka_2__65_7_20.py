class DynamicList:

    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def get_by_position(self, position):
        if position < 0 or position >= len(self.elements):
            raise ValueError('Position out of range')
        return self.elements[position]
if __name__ == '__main__':
    dynamic_list = DynamicList()
    dynamic_list.add(10)
    dynamic_list.add(20)
    dynamic_list.add(30)
    try:
        print(dynamic_list.get_by_position(1))
    except ValueError as e:
        print(e)