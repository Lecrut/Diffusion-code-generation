class ArrayHandler:
    def __init__(self, array):
        self.array = array

    def get_last_element(self):
        return self.array[-1]

if __name__ == '__main__':
    sample_array = [7, 8, 9, 10, 11]
    handler = ArrayHandler(sample_array)
    print(handler.get_last_element())