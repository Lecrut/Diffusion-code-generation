class ListPrinter:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = 0

    def print_until_condition(self, condition):
        while self.index < len(self.data_list) and not condition(self.data_list[self.index]):
            print(self.data_list[self.index])
            self.index += 1

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    printer = ListPrinter(sample_list)
    printer.print_until_condition(lambda x: isinstance(x, str))