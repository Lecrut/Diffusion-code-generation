class CustomList:

    def __init__(self):
        self.elements = []

    def add(self, item):
        self.elements.append(item)

    def get(self, index):
        return self.elements[index]
if __name__ == '__main__':
    custom_list = CustomList()
    custom_list.add(10)
    custom_list.add(20)
    custom_list.add(30)
    print(custom_list.get(1))