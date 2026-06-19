class ElementAccessor:

    def __init__(self, items):
        self.items = items

    @classmethod
    def get_first_element(cls, instance):
        if not cls._is_valid_list(instance.items):
            raise ValueError('The list is empty')
        return instance.items[0]

    @staticmethod
    def _is_valid_list(lst):
        return bool(lst)
if __name__ == '__main__':
    sample_list1 = [5, 15, 25]
    sample_list2 = ['x', 'y', 'z']
    empty_list = []
    accessor1 = ElementAccessor(sample_list1)
    accessor2 = ElementAccessor(sample_list2)
    accessor3 = ElementAccessor(empty_list)
    try:
        print(ElementAccessor.get_first_element(accessor1))
        print(ElementAccessor.get_first_element(accessor2))
        print(ElementAccessor.get_first_element(accessor3))
    except ValueError as e:
        print(f'Caught expected error for empty list: {e}')