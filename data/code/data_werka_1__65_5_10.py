class FastAccessList:

    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError('Elements must be provided as a list')
        self.elements = elements

    def get_element(self, index):
        try:
            return self.elements[index]
        except IndexError:
            raise IndexError('Index out of bounds')
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    fast_list = FastAccessList(sample_data)
    try:
        print(fast_list.get_element(0))
        print(fast_list.get_element(2))
        print(fast_list.get_element(4))
        print(fast_list.get_element(-1))
    except IndexError as e:
        print(e)