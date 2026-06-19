class FastList:
    def __init__(self, elements):
        self.elements = list(elements)

    def get(self, index):
        try:
            return self.elements[index]
        except IndexError:
            raise IndexError("Index out of range")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    fast_list = FastList(sample_data)
    
    print(f"Element at index 0: {fast_list.get(0)}")
    print(f"Element at index 2: {fast_list.get(2)}")
    try:
        print(f"Element at index 10: {fast_list.get(10)}")
    except IndexError as e:
        print(e)