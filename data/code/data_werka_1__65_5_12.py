class FastAccessList:

    def __init__(self, elements):
        self.elements = list(elements)

    def get_element(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index < 0 or index >= len(self.elements):
            raise IndexError('Index out of bounds')
        return self.elements[index]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    fast_list = FastAccessList(sample_data)
    try:
        print(fast_list.get_element(0))
        print(fast_list.get_element(2))
        print(fast_list.get_element(4))
        print(fast_list.get_element(-1))
    except (TypeError, IndexError) as e:
        print(e)