class ListChecker:
    def contains(self, item, data_list):
        return item in data_list
if __name__ == '__main__':
    checker = ListChecker()
    sample_list = [1, 5, 10, 15, 20]
    item_to_find_present = 10
    item_to_find_absent = 7
    result_present = checker.contains(item_to_find_present, sample_list)
    result_absent = checker.contains(item_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {item_to_find_present}? {result_present}")
    print(f"Does the list {sample_list} contain {item_to_find_absent}? {result_absent}")