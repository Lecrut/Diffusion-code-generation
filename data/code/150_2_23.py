class ListModifier:
    def __init__(self, data):
        self.data = data

    @classmethod
    def remove_all_instances(cls, lst, value):
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == value:
                del lst[i]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 2]
    modifier = ListModifier(sample_list)
    ListModifier.remove_all_instances(modifier.data, 2)
    print(modifier.data)