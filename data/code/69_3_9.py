class ListIndexPrinter:
    def __init__(self, data):
        self.data = data

    def print_element_at_index(self, index):
        try:
            if not isinstance(index, int):
                raise TypeError("Index must be an integer.")
            if index < 0 or index >= len(self.data):
                raise IndexError("Index out of range.")
            return self.data[index]
        except (TypeError, IndexError) as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    printer = ListIndexPrinter(sample_list)
    
    index_to_check = 2
    element = printer.print_element_at_index(index_to_check)
    if element is not None:
        print(f"Element at index {index_to_check}: {element}")
    
    invalid_index = -1
    element = printer.print_element_at_index(invalid_index)
    if element is not None:
        print(f"Element at index {invalid_index}: {element}")
    
    non_integer_index = "five"
    element = printer.print_element_at_index(non_integer_index)
    if element is not None:
        print(f"Element at index '{non_integer_index}': {element}")