class ListChecker:
    def contains(self, item, data_list):
        return item in data_list
if __name__ == '__main__':
    checker = ListChecker()
    sample_list = [1, 2, 3, 4, 5]
    item_to_find_present = 3
    item_to_find_absent = 9
    result1 = checker.contains(item_to_find_present, sample_list)
    print(f"Does {sample_list} contain {item_to_find_present}? {result1}")
    result2 = checker.contains(item_to_find_absent, sample_list)
    print(f"Does {sample_list} contain {item_to_find_absent}? {result2}")