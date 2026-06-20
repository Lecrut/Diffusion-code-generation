class ListProcessor:
    def __init__(self, data):
        self.data = data

    def find_middle_element(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    processor = ListProcessor(sample_list)
    result = processor.find_middle_element()
    print(result)