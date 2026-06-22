class ArrayUtils:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_last(self):
        if not self.elements:
            raise IndexError("Cannot get the last item from an empty list")
        return self.elements[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    array_utils_instance = ArrayUtils(sample_list)
    try:
        print(array_utils_instance.retrieve_last())
    except IndexError as e:
        print(f"Error: {e}")