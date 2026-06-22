class CustomList:

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, index):
        try:
            return self.elements[index]
        except IndexError:
            raise IndexError('Index out of range')
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    custom_list = CustomList(sample_data)
    print(custom_list.get_element(0))
    print(custom_list.get_element(5))
    print(custom_list.get_element(-1))