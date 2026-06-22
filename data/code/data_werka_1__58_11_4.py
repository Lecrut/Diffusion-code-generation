class ElementAccessor:

    def __init__(self, data):
        self.data = data

    @classmethod
    def get_first_element(cls, instance):
        if not instance.data:
            raise IndexError('The list is empty')
        return instance.data[0]
if __name__ == '__main__':
    sample_list1 = [5, 10, 15]
    sample_list2 = ['x', 'y', 'z']
    empty_list = []
    accessor1 = ElementAccessor(sample_list1)
    accessor2 = ElementAccessor(sample_list2)
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
        ElementAccessor.get_first_element(accessor3)
    except IndexError as e:
        print('Caught expected error for empty list:', e)