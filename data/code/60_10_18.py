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
        last_element = array_utils_instance.retrieve_last()
        print(f"The last element of {sample_list} is: {last_element}")
        
        empty_list = []
        array_utils_empty = ArrayUtils(empty_list)
        last_element_empty = array_utils_empty.retrieve_last()
        print(f"The last element of an empty list is: {last_element_empty}")
    except IndexError as e:
        print(e)