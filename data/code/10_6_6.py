class ArrayProcessor:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        return self.data[0]

if __name__ == '__main__':
    processor = ArrayProcessor([1, 2, 3, 4, 5])
    print(processor.get_first_element())