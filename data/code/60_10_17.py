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
        result = array_utils_instance.retrieve_last()
        print(f"The last item of {sample_list} is: {result}")
    except IndexError as e:
        print(f"Error for empty list: {e}")