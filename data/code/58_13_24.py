class ListProcessor:
    def __init__(self, data):
        self.data = data
    def validate_data(self):
        if not isinstance(self.data, list):
            raise TypeError("Data must be a list.")
        if len(self.data) == 0:
            raise ValueError("The list is empty and has no first element.")
    def fetch_first_element(self):
        return self.data[0]

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    processor = ListProcessor(sample_list)
    try:
        processor.validate_data()
        first_element = processor.fetch_first_element()
        print(first_element)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")