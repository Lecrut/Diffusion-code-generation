class ListElementPrinter:
    @staticmethod
    def print_element_at_index(data_list, index):
        try:
            element = data_list[index]
            print(f"Element at index {index}: {element}")
        except IndexError:
            print(f"IndexError: Index {index} is out of range for the list.")
        except TypeError:
            print("TypeError: The first argument must be a list and the second must be an integer.")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    ListElementPrinter.print_element_at_index(sample_list, 2)
    ListElementPrinter.print_element_at_index(sample_list, 5)
    ListElementPrinter.print_element_at_index("not a list", 0)