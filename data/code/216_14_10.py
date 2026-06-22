class SequenceProcessor:
    def __init__(self, data):
        self.data = data

    def find_central_element(self):
        length = len(self.data)
        central_index = length // 2
        return self.data[central_index]

if __name__ == '__main__':
    processor1 = SequenceProcessor([7, 3, 1, 8, 4, 9])
    print(processor1.find_central_element())