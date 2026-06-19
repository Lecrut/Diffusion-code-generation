class ListElementPrinter:
    @staticmethod
    def print_element_at_index(data, index):
        try:
            element = data[index]
            print(element)
        except IndexError:
            print("Index out of range")
        except TypeError:
            print("Invalid input type")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    ListElementPrinter.print_element_at_index(sample_list, 2)
    ListElementPrinter.print_element_at_index(sample_list, 5)
    ListElementPrinter.print_element_at_index("Hello", 1)
    ListElementPrinter.print_element_at_index(12345, 0)