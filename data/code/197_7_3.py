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
    items_list_a = ["apple", "banana", "cherry"]
    items_list_b = ["banana", "date", "elderberry"]
    items_list_c = ["fig", "grape", "apple"]
    store.add_to_list("apple", "ListA")
    store.add_to_list("banana", "ListA")
    store.add_to_list("cherry", "ListA")
    store.add_to_list("banana", "ListB")
    store.add_to_list("date", "ListB")
    store.add_to_list("elderberry", "ListB")
    store.add_to_list("fig", "ListC")
    store.add_to_list("grape", "ListC")
    store.add_to_list("apple", "ListC")
    print(f"Is 'apple' a member of any list? {store.is_member('apple')}")
    print(f"Is 'banana' a member of any list? {store.is_member('banana')}")
    print(f"Is 'date' a member of any list? {store.is_member('date')}")
    print(f"Is 'fig' a member of any list? {store.is_member('fig')}")
    print(f"Is 'kiwi' a member of any list? {store.is_member('kiwi')}")