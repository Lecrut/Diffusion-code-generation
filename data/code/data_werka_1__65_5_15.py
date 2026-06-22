class FastAccessList:

    def __init__(self):
        self.elements = []

    def append(self, value):
        self.elements.append(value)

    def get(self, index):
        return self.elements[index]
if __name__ == '__main__':
    fast_list = FastAccessList()
    fast_list.append(10)
    fast_list.append(20)
    fast_list.append(30)
    print(fast_list.get(1))