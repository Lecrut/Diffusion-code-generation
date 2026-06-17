class ListPrinter:
    @staticmethod
    def print_list(data):
        for item in data:
            print(item)
if __name__ == '__main__':
    my_list = [1, "hello", 3.14, True]
    ListPrinter.print_list(my_list)