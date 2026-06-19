class ListManager:
    EMPTY_LIST_ERROR_MESSAGE = "The list is empty"

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def get_first_element(cls, instance):
        if not instance.elements:
            raise ValueError(cls.EMPTY_LIST_ERROR_MESSAGE)
        return instance.elements[0]

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25]
    sample_list_2 = ['x', 'y', 'z']
    empty_list = []

    manager_1 = ListManager(sample_list_1)
    manager_2 = ListManager(sample_list_2)
    empty_manager = ListManager(empty_list)

    try:
        print(ListManager.get_first_element(manager_1))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print(ListManager.get_first_element(manager_2))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print(ListManager.get_first_element(empty_manager))
    except ValueError as e:
        print(f"Error: {e}")