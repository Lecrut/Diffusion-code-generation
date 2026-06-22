class ElementAccessor:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def get_first_element(cls, instance):
        if not instance.elements:
            raise IndexError("list is empty")
        return instance.elements[0]

if __name__ == '__main__':
    list1 = [5, 15, 25, 35]
    list2 = ['x', 'y', 'z']
    empty_list = []

    accessor1 = ElementAccessor(list1)
    accessor2 = ElementAccessor(list2)
    accessor3 = ElementAccessor(empty_list)

    try:
        print(ElementAccessor.get_first_element(accessor1))
    except IndexError as e:
        print(e)

    try:
        print(ElementAccessor.get_first_element(accessor2))
    except IndexError as e:
        print(e)

    try:
        print(ElementAccessor.get_first_element(accessor3))
    except IndexError as e:
        print(e)