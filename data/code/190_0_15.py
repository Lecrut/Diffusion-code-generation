class ListChecker:
    def __init__(self, input_list):
        self.data_set = set(input_list)

    def check_item(self, item):
        return item in self.data_set

if __name__ == '__main__':
    my_checker = ListChecker([1, 5, 8, 10, 2])
    print(f"Is 8 in the list? {my_checker.check_item(8)}")
    print(f"Is 9 in the list? {my_checker.check_item(9)}")