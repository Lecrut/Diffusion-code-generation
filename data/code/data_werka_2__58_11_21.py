class ListAccessor:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Elements must be a list")
        self.elements = elements

    @classmethod
    def get_first_element(cls, instance):
        if not isinstance(instance, cls):
            raise ValueError("Instance must be of type ListAccessor")
        return instance.elements[0] if instance.elements else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    accessor = ListAccessor(sample_list)
    print(ListAccessor.get_first_element(accessor))