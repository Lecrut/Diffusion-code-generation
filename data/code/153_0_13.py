class ItemExistenceChecker:
    @staticmethod
    def check_item_existence(item, string_list):
        return item in string_list

if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    checker = ItemExistenceChecker()
    result = checker.check_item_existence(target_item, data_list)
    print(f"Does '{target_item}' exist in the list? {result}")