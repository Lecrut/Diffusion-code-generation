class ListModifier:

    def __init__(self, initial_list):
        self.data = initial_list

    @classmethod
    def remove_all(cls, lst, value):
        while value in lst:
            lst.remove(value)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    modifier = ListModifier(sample_list)
    ListModifier.remove_all(modifier.data, 2)
    print(modifier.data)