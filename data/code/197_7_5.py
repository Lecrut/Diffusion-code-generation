class MembershipChecker:
    def __init__(self):
        self.membership_sets = {}
    def add_list(self, list_name, items):
        self.membership_sets[list_name] = set(items)
    def is_member(self, list_name, item):
        if list_name in self.membership_sets:
            return item in self.membership_sets[list_name]
        return False
if __name__ == '__main__':
    checker = MembershipChecker()
    list1_items = ["apple", "banana", "cherry"]
    list2_items = ["date", "elderberry", "fig"]
    checker.add_list("fruits_a", list1_items)
    checker.add_list("fruits_b", list2_items)
    print(f"Is 'apple' in fruits_a? {checker.is_member('fruits_a', 'apple')}")
    print(f"Is 'date' in fruits_a? {checker.is_member('fruits_a', 'date')}")
    print(f"Is 'fig' in fruits_b? {checker.is_member('fruits_b', 'fig')}")
    print(f"Is 'grape' in fruits_a? {checker.is_member('fruits_a', 'grape')}")
    print(f"Is 'banana' in fruits_b? {checker.is_member('fruits_b', 'banana')}")
    print(f"Is 'apple' in non_existent_list? {checker.is_member('non_existent_list', 'apple')}")