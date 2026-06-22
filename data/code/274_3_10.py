class NestedListPrinter:
    def print_items(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                self.print_items(item)
            else:
                print(item)

if __name__ == '__main__':
    printer = NestedListPrinter()
    sample = [1, [2, 3], [4, [5, 6]]]
    printer.print_items(sample)