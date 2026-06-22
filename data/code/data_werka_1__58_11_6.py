class ListManager:
    def __init__(self, items):
        self.items = items

    @classmethod
    def get_first(cls, instance):
        if not instance.items:
            raise ValueError("The list is empty")
        return instance.items[0]

if __name__ == '__main__':
    sample_list1 = [5, 6, 7, 8]
    sample_list2 = ['x', 'y', 'z']
    empty_list = []
    
    manager1 = ListManager(sample_list1)
    manager2 = ListManager(sample_list2)
    empty_manager = ListManager(empty_list)

    print(ListManager.get_first(manager1))
    print(ListManager.get_first(manager2))

    try:
        ListManager.get_first(empty_manager)
    except ValueError as e:
        print(e)