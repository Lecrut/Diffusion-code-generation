class ListContainer:
    def __init__(self):
        self._internal_list = [10, 20, 30, 40, 50]

    @classmethod
    def get_second_element(cls):
        instance = cls()
        return instance._internal_list[1]

if __name__ == '__main__':
    second_element = ListContainer.get_second_element()
    print(second_element)