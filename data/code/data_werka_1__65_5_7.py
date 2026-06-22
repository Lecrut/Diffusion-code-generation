class FastList:

    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def get(self, index):
        return self.data[index]
if __name__ == '__main__':
    fast_list = FastList()
    fast_list.append(10)
    fast_list.append(20)
    fast_list.append(30)
    print(fast_list.get(1))