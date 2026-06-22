class UniqueElementsPrinter:
    @staticmethod
    def print_unique_elements(elements):
        unique_elements = set(elements)
        for element in unique_elements:
            print(element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3]
    UniqueElementsPrinter.print_unique_elements(sample_list)