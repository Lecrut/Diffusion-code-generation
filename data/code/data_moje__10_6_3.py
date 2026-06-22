class ArrayProcessor:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        return self.data[0]

if __name__ == '__main__':
    processor = ArrayProcessor([10, 20, 30])
    print(processor.get_first_element())