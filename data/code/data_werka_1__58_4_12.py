class ListProcessor:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_string(cls, string_data):
        if not isinstance(string_data, str):
            raise ValueError("Input must be a string.")
        return cls(string_data.split())

    def get_first_element(self):
        if not self.data:
            raise IndexError("List is empty.")
        return self.data[0]

if __name__ == '__main__':
    try:
        sample_list = [10, 20, 30, 40]
        processor = ListProcessor(sample_list)
        first_element = processor.get_first_element()
        print(first_element)

        string_list_processor = ListProcessor.from_string("apple banana cherry")
        first_element_from_string = string_list_processor.get_first_element()
        print(first_element_from_string)

    except Exception as e:
        print(f"An error occurred: {e}")