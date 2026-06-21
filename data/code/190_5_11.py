class ListMembershipChecker:
    @staticmethod
    def contains(data_list, item):
        return item in data_list

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400]
    item_to_find_present = 300
    item_to_find_absent = 900
    empty_list = []
    
    checker = ListMembershipChecker()
    result1 = checker.contains(sample_list, item_to_find_present)
    print(f"Does {sample_list} contain {item_to_find_present}? {result1}")
    result2 = checker.contains(sample_list, item_to_find_absent)
    print(f"Does {sample_list} contain {item_to_find_absent}? {result2}")
    result3 = checker.contains(empty_list, 50)
    print(f"Does {empty_list} contain 50? {result3}")