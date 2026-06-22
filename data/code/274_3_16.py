class NestedListPrinter:
    @staticmethod
    def print_item(item):
        if isinstance(item, list):
            NestedListPrinter.print_nested_list(item)
        else:
            print(item)

    @staticmethod
    def print_nested_list(nested_list):
        for item in nested_list:
            NestedListPrinter.print_item(item)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    NestedListPrinter.print_nested_list(sample)