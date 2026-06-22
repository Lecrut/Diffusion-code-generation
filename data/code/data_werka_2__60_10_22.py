class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_last(self):
        if not self.elements:
            return None
        last_element = self.elements[-1]
        return last_element

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    array_utils_instance = ArrayUtils(sample_data)
    result = array_utils_instance.retrieve_last()
    print(result)