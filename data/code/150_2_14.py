class ListModifier:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        elif not isinstance(initial_data, list):
            raise ValueError("Initial data must be a list")
        self.items = initial_data

    @classmethod
    def remove_all_instances(cls, lst, item):
        while item in lst:
            lst.remove(item)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    modifier = ListModifier(sample_list)
    ListModifier.remove_all_instances(modifier.items, 2)
    print("Modified list:", modifier.items)