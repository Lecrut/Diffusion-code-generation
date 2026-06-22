class FastList:

    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError('Index out of range')
if __name__ == '__main__':
    fast_list = FastList()
    fast_list.add(10)
    fast_list.add(20)
    fast_list.add(30)
    print(fast_list.get(1))