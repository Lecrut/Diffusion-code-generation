class ListManager:
    EMPTY_LIST_ERROR = "The list is empty"

    def __init__(self, elements):
        self.elements = elements

    @staticmethod
    def get_first_element(instance):
        if instance.elements:
            return instance.elements[0]
        else:
            raise ValueError(ListManager.EMPTY_LIST_ERROR)

if __name__ == '__main__':
    sample_list1 = [5, 15, 25, 35]
    sample_list2 = ['x', 'y', 'z']
    empty_list = []

    manager1 = ListManager(sample_list1)
    manager2 = ListManager(sample_list2)
    manager_empty = ListManager(empty_list)

    print(ListManager.get_first_element(manager1))
    print(ListManager.get_first_element(manager2))

    try:
        ListManager.get_first_element(manager_empty)
    except ValueError as e:
        print(e)