class ListFinder:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        self._internal_list = data

    def get_first_element(self):
        try:
            return self._internal_list[0]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    finder = ListFinder(sample_data)
    first_element = finder.get_first_element()
    print(first_element)

    sample_data_empty = []
    finder_empty = ListFinder(sample_data_empty)
    first_element_empty = finder_empty.get_first_element()
    print(first_element_empty)

    invalid_input = "not a list"
    try:
        finder_invalid = ListFinder(invalid_input)
    except ValueError as e:
        print(e)