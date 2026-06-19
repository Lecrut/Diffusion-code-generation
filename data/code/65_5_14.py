class CustomList:

    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError('Elements must be provided as a list')
        self.elements = elements

    def get_element(self, index):
        try:
            return self.elements[index]
        except IndexError:
            raise IndexError('Index out of range')
if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    custom_list = CustomList(sample_data)
    try:
        print(custom_list.get_element(0))
        print(custom_list.get_element(2))
        print(custom_list.get_element(4))
        print(custom_list.get_element(5))
    except IndexError as e:
        print(e)