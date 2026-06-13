class ListChecker:
    @staticmethod
    def contains(data_list, item):
        return item in data_list
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    item_to_find_present = 30
    item_to_find_absent = 99
    empty_list = []
    print(f"Checking if {item_to_find_present} is in {sample_list}: {ListChecker.contains(sample_list, item_to_find_present)}")
    print(f"Checking if {item_to_find_absent} is in {sample_list}: {ListChecker.contains(sample_list, item_to_find_absent)}")
    print(f"Checking if {item_to_find_present} is in an empty list: {ListChecker.contains(empty_list, item_to_find_present)}")