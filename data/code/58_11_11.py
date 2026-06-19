class ListProcessor:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def get_first_element(cls, instance):
        if not instance.elements:
            raise IndexError("The list is empty")
        return instance.elements[0]

if __name__ == '__main__':
    sample_list1 = [5, 15, 25, 35]
    sample_list2 = ['x', 'y', 'z']
    empty_list = []

    processor1 = ListProcessor(sample_list1)
    try:
        print(f"First element of {sample_list1}: {ListProcessor.get_first_element(processor1)}")
    except IndexError as e:
        print(e)

    processor2 = ListProcessor(sample_list2)
    try:
        print(f"First element of {sample_list2}: {ListProcessor.get_first_element(processor2)}")
    except IndexError as e:
        print(e)

    empty_processor = ListProcessor(empty_list)
    try:
        print(f"First element of an empty list: {ListProcessor.get_first_element(empty_processor)}")
    except IndexError as e:
        print(f"Caught expected error for empty list: {e}")