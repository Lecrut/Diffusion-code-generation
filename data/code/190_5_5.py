class ListChecker:
    @staticmethod
    def contains(data_list, item):
        return item in data_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_find_present = 3
    item_to_find_absent = 99
    empty_list = []
    item_to_find_in_empty = 1
    print(f"Checking if {item_to_find_present} is in {sample_list}: {ListChecker.contains(sample_list, item_to_find_present)}")
    print(f"Checking if {item_to_find_absent} is in {sample_list}: {ListChecker.contains(sample_list, item_to_find_absent)}")
    print(f"Checking if {item_to_find_in_empty} is in an empty list: {ListChecker.contains(empty_list, item_to_find_in_empty)}")