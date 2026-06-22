class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def _validate_non_empty(self):
        if not self.elements:
            raise IndexError("Cannot get the last item from an empty list")

    def retrieve_last(self):
        self._validate_non_empty()
        return self.elements[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    array_utils_instance = ArrayUtils(sample_list)
    try:
        last_element = array_utils_instance.retrieve_last()
        print(f"The last element of {sample_list} is: {last_element}")
    except IndexError as e:
        print(e)

    empty_list = []
    array_utils_empty = ArrayUtils(empty_list)
    try:
        last_element_empty = array_utils_empty.retrieve_last()
        print(last_element_empty)
    except IndexError as e:
        print(f"Error for empty list: {e}")