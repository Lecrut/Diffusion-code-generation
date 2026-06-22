class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def _validate_not_empty(self):
        if not self.elements:
            raise IndexError("Cannot get the last item from an empty list")

    def retrieve_last(self):
        self._validate_not_empty()
        return self.elements[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    array_utils_instance = ArrayUtils(sample_list)
    try:
        last_element = array_utils_instance.retrieve_last()
        print(f"The last element is: {last_element}")
    except IndexError as e:
        print(e)

    empty_list = []
    empty_array_utils_instance = ArrayUtils(empty_list)
    try:
        last_element_empty = empty_array_utils_instance.retrieve_last()
        print(f"The last element is: {last_element_empty}")
    except IndexError as e:
        print(e)