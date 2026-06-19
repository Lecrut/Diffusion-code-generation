class CustomList:

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]
if __name__ == '__main__':
    sample_list = CustomList([10, 20, 30, 40, 50])
    print(sample_list[2])