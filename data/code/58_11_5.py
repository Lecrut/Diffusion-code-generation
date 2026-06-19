class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def get_first_element(cls, instance):
        if instance.elements:
            return instance.elements[0]
        else:
            raise ValueError("The list is empty")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor_instance = ListAccessor(sample_list)
    print(ListAccessor.get_first_element(accessor_instance))