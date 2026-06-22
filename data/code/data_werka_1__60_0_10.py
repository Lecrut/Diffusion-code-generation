class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_last_element(self):
        if not self.data:
            return None
        return self.data[-1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    processor = ListProcessor(sample_list)
    last_element = processor.get_last_element()
    print(last_element)