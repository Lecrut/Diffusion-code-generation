class MembershipStore:
    def __init__(self):
        self.membership_lists = {}
    def add_list(self, list_name, items):
        self.membership_lists[list_name] = set(items)
    def is_member(self, item):
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
    print(f"Is 'banana' a member of any list? {store.is_member('banana')}")
    print(f"Is 'apple' a member of any list? {store.is_member('apple')}")
    print(f"Is 'date' a member of any list? {store.is_member('date')}")
    print(f"Is 'fig' a member of any list? {store.is_member('fig')}")
    print(f"Is 'kiwi' a member of any list? {store.is_member('kiwi')}")