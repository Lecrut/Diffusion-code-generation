class ListProcessor:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_csv(cls, csv_string):
        return cls(csv_string.split(','))

    def get_first_element(self):
        if not isinstance(self.data, list) or len(self.data) == 0:
            raise ValueError("Data must be a non-empty list")
        return self.data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    processor = ListProcessor(sample_list)
    try:
        first_element = processor.get_first_element()
        print(first_element)
    except ValueError as e:
        print(e)

    csv_string = "red,green,blue"
    csv_processor = ListProcessor.from_csv(csv_string)
    try:
        first_element_from_csv = csv_processor.get_first_element()
        print(first_element_from_csv)
    except ValueError as e:
        print(e)