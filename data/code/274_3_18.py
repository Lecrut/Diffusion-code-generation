class NestedListPrinter:

    @staticmethod
    def print_item(item):
        print(item)

    @classmethod
    def print_nested(cls, data):
        for item in data:
            if isinstance(item, list):
                cls.print_nested(item)
            else:
                cls.print_item(item)
if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    printer = NestedListPrinter()
    printer.print_nested(sample_data)