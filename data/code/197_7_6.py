class MembershipStore:
    def __init__(self):
        self.membership_lists = {}
    def add_list(self, list_name, items):
        self.membership_lists[list_name] = set(items)
    def check_membership(self, item):
        for list_name in self.membership_lists:
            if item in self.membership_lists[list_name]:
                return True
        return False
if __name__ == '__main__':
    store = MembershipStore()
    list1_items = ["apple", "banana", "cherry"]
    list2_items = ["date", "banana", "elderberry"]
    list3_items = ["fig", "grape"]
    store.add_list("fruits_a", list1_items)
    store.add_list("fruits_b", list2_items)
    store.add_list("fruits_c", list3_items)
    print(f"Is 'banana' in any list? {store.check_membership('banana')}")
    print(f"Is 'apple' in any list? {store.check_membership('apple')}")
    print(f"Is 'date' in any list? {store.check_membership('date')}")
    print(f"Is 'fig' in any list? {store.check_membership('fig')}")
    print(f"Is 'zoo' in any list? {store.check_membership('zoo')}")