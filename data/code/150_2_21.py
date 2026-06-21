class ListModifier:
    def __init__(self, initial_data):
        self.data = initial_data

    @classmethod
    def remove_all_instances(cls, lst, item):
        while item in lst:
            lst.remove(item)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 20, 60]
    modifier = ListModifier(sample_list)
    ListModifier.remove_all_instances(modifier.data, 20)
    print("Modified list:", modifier.data)