class CustomList:

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        if not 0 <= index < len(self.elements):
            raise IndexError('Index out of range')
        return self.elements[index]
if __name__ == '__main__':
    sample_list = CustomList([10, 20, 30, 40, 50])
    print(sample_list[2])
    print(sample_list[0])
    try:
        print(sample_list[5])
    except IndexError as e:
        print(e)