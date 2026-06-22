class ListManager:
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_first_element(cls, instance):
        if not instance.data:
            raise IndexError("The list is empty")
        return instance.data[0]

if __name__ == '__main__':
    sample_data1 = [5, 15, 25, 35]
    sample_data2 = ['x', 'y', 'z']
    empty_data = []

    manager1 = ListManager(sample_data1)
    manager2 = ListManager(sample_data2)
    empty_manager = ListManager(empty_data)

    try:
        print(ListManager.get_first_element(manager1))
    except IndexError as e:
        print(e)

    try:
        print(ListManager.get_first_element(manager2))
    except IndexError as e:
        print(e)

    try:
        print(ListManager.get_first_element(empty_manager))
    except IndexError as e:
        print(e)