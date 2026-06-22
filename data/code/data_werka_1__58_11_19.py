class ListHandler:
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_first_element(cls, instance):
        if not instance.data:
            raise ValueError("The list is empty")
        return instance.data[0]

if __name__ == '__main__':
    sample_list1 = [5, 10, 15]
    sample_list2 = ['x', 'y', 'z']
    empty_list = []

    handler1 = ListHandler(sample_list1)
    handler2 = ListHandler(sample_list2)
    empty_handler = ListHandler(empty_list)

    try:
        first_element1 = ListHandler.get_first_element(handler1)
        print(f"First element of sample_list1: {first_element1}")
    except ValueError as e:
        print(e)

    try:
        first_element2 = ListHandler.get_first_element(handler2)
        print(f"First element of sample_list2: {first_element2}")
    except ValueError as e:
        print(e)

    try:
        ListHandler.get_first_element(empty_handler)
    except ValueError as e:
        print(f"Error for empty list: {e}")