class ListProcessor:
    def __init__(self, data):
        self._internal_list = list(data)
    
    def get_last_element(self):
        if not self._internal_list:
            raise ValueError("The internal list is empty.")
        return self._internal_list[-1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    processor = ListProcessor(sample_data)
    try:
        last_element = processor.get_last_element()
        print(last_element)
    except ValueError as e:
        print(e)

    sample_data_empty = []
    processor_empty = ListProcessor(sample_data_empty)
    try:
        last_element_empty = processor_empty.get_last_element()
        print(last_element_empty)
    except ValueError as e:
        print(e)