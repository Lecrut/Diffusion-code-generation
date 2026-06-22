class NestedListPrinter:
    @staticmethod
    def print_item(item):
        print(item)

    @classmethod
    def print_nested_list(cls, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                cls.print_nested_list(item)
            else:
                cls.print_item(item)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]]]
    NestedListPrinter.print_nested_list(sample)