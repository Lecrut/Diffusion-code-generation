class ListFinder:
    def __init__(self, data):
        self._internal_list = data

    def _validate_data(self):
        if not isinstance(self._internal_list, list):
            raise ValueError("Data must be a list")

    def get_first_element(self):
        self._validate_data()
        if not self._internal_list:
            return None
        return self._internal_list[0]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35]
    finder = ListFinder(sample_data)
    first_element = finder.get_first_element()
    print(first_element)

    sample_data_empty = []
    finder_empty = ListFinder(sample_data_empty)
    first_element_empty = finder_empty.get_first_element()
    print(first_element_empty)

    sample_data_invalid = "not a list"
    try:
        invalid_finder = ListFinder(sample_data_invalid)
        invalid_first_element = invalid_finder.get_first_element()
        print(invalid_first_element)
    except ValueError as e:
        print(e)