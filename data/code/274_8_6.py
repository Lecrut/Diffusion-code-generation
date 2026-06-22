class ListPrinter:
    MAX_RETRIES = 5

    @staticmethod
    def print_until_condition(my_list, condition):
        retries = 0
        index = 0
        while index < len(my_list) and not condition(my_list[index]) and retries < ListPrinter.MAX_RETRIES:
            print(my_list[index])
            index += 1
            retries += 1

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    condition = lambda x: isinstance(x, str)
    ListPrinter.print_until_condition(sample_list, condition)