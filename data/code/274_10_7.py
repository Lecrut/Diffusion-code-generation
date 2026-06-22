class ListPrinter:
    @staticmethod
    def print_items(lst):
        for item in lst:
            print(item)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    ListPrinter.print_items(sample_list)