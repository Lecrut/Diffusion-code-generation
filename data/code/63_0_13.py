class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        if not self.data:
            raise ValueError("The list is empty")
        return self.data[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    processor = ListProcessor(sample_list)
    try:
        first_value = processor.get_first_element()
        print(first_value)
    except ValueError as e:
        print(e)