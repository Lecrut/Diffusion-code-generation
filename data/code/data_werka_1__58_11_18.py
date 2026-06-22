class ElementAccessor:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def get_first_element(cls, instance):
        if not isinstance(instance, cls):
            raise ValueError("Instance must be an instance of ElementAccessor")
        return instance.elements[0] if instance.elements else None

if __name__ == '__main__':
    sample_elements = [10, 20, 30, 40]
    accessor_instance = ElementAccessor(sample_elements)
    print(ElementAccessor.get_first_element(accessor_instance))