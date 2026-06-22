class ElementPrinter:
    INVALID_INDEX_TYPE_MESSAGE = "Invalid index type"
    INDEX_OUT_OF_RANGE_MESSAGE = "Index out of range"

    @staticmethod
    def is_valid_index(index):
        return isinstance(index, int)

    def __init__(self, data_list):
        if not isinstance(data_list, list):
            raise ValueError("The first argument must be a list.")
        self.data_list = data_list

    def print_element_at_index(self, index):
        try:
            if not ElementPrinter.is_valid_index(index):
                raise TypeError(ElementPrinter.INVALID_INDEX_TYPE_MESSAGE)
            if index < 0 or index >= len(self.data_list):
                raise IndexError(ElementPrinter.INDEX_OUT_OF_RANGE_MESSAGE)
            return self.data_list[index]
        except (TypeError, IndexError) as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    printer = ElementPrinter(sample_list)
    
    valid_index = 2
    element = printer.print_element_at_index(valid_index)
    if element is not None:
        print(f"Element at index {valid_index}: {element}")

    invalid_index = 10
    element = printer.print_element_at_index(invalid_index)
    if element is not None:
        print(f"Element at index {invalid_index}: {element}")

    non_integer_index = 'a'
    element = printer.print_element_at_index(non_integer_index)
    if element is not None:
        print(f"Element at index {non_integer_index}: {element}")