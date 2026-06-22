class FastIndexedList:

    def __init__(self, elements):
        self.elements = list(elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __len__(self):
        return len(self.elements)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    fast_list = FastIndexedList(sample_data)
    print(fast_list[0])
    print(fast_list[2])
    print(fast_list[len(fast_list) - 1])