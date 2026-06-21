class ListChecker:
    def __init__(self, input_list):
        self.set_data = set(input_list)

    def check_item(self, item):
        return item in self.set_data

if __name__ == '__main__':
    checker = ListChecker([1, 5, 8, 10, 2])
    item_to_find_present = 8
    item_to_find_absent = 9
    print(f"Is {item_to_find_present} in the list? {checker.check_item(item_to_find_present)}")
    print(f"Is {item_to_find_absent} in the list? {checker.check_item(item_to_find_absent)}")