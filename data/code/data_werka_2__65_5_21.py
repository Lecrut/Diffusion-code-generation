class FastList:

    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def get_element(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError('Index out of bounds')
        return self.data[index]
if __name__ == '__main__':
    fast_list = FastList()
    fast_list.add(15)
    fast_list.add(25)
    fast_list.add(35)
    try:
        print(fast_list.get_element(0))
        print(fast_list.get_element(2))
        print(fast_list.get_element(4))
    except IndexError as e:
        print(e)