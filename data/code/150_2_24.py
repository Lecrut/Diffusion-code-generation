class ListModifier:

    def __init__(self, data):
        self.data = data

    @classmethod
    def remove_all(cls, lst, value):
        while value in lst:
            lst.remove(value)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 2, 3]
    modifier = ListModifier(sample_list)
    modifier.remove_all(3)
    print(modifier.data)