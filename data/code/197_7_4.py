import collections
class MembershipStore:
    def __init__(self):
        self.membership_lists = collections.defaultdict(set)
    def add_to_list(self, item, list_name):
        self.membership_lists[list_name].add(item)
    def is_member(self, item):
        for list_name in self.membership_lists:
            if item in self.membership_lists[list_name]:
                return True
        return False
if __name__ == '__main__':
    store = MembershipStore()
    items1 = ["apple", "banana", "cherry"]
    items2 = ["banana", "date", "elderberry"]
    items3 = ["fig", "grape"]
    store.add_to_list("apple", "fruits_a")
    store.add_to_list("banana", "fruits_a")
    store.add_to_list("cherry", "fruits_a")
    store.add_to_list("banana", "fruits_b")
    store.add_to_list("date", "fruits_b")
    store.add_to_list("elderberry", "fruits_b")
    store.add_to_list("fig", "fruits_c")
    store.add_to_list("grape", "fruits_c")
    print(f"Is 'banana' a member of any list? {store.is_member('banana')}")
    print(f"Is 'apple' a member of any list? {store.is_member('apple')}")
    print(f"Is 'date' a member of any list? {store.is_member('date')}")
    print(f"Is 'fig' a member of any list? {store.is_member('fig')}")
    print(f"Is 'zucchini' a member of any list? {store.is_member('zucchini')}")