class MembershipChecker:
    def __init__(self):
        self.membership_data = {}
    def add_list(self, list_name, items):
        self.membership_data[list_name] = set(items)
    def check_membership(self, item):
        for list_name in self.membership_data:
            if item in self.membership_data[list_name]:
                return True
        return False
if __name__ == '__main__':
    checker = MembershipChecker()
    list1_items = ["apple", "banana", "cherry"]
    list2_items = ["date", "banana", "elderberry"]
    list3_items = ["fig", "grape"]
    checker.add_list("fruits_a", list1_items)
    checker.add_list("fruits_b", list2_items)
    checker.add_list("fruits_c", list3_items)
    print(f"Is 'banana' in any list? {checker.check_membership('banana')}")
    print(f"Is 'apple' in any list? {checker.check_membership('apple')}")
    print(f"Is 'grape' in any list? {checker.check_membership('grape')}")
    print(f"Is 'kiwi' in any list? {checker.check_membership('kiwi')}")