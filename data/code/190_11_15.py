class ListChecker:
    @staticmethod
    def contains_item(item_list, target):
        return target in item_list

if __name__ == '__main__':
    sample_list = [10, 25, 33, 42, 56, 78, 91]
    target_number = 42
    result = ListChecker.contains_item(sample_list, target_number)
    print(f"The number {target_number} {'exists' if result else 'does not exist'} in the list.")