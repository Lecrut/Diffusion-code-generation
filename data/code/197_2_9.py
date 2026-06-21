class MembershipChecker:
    def __init__(self, list1, list2):
        self._list1 = set(list1)
        self._list2 = set(list2)

    def get_common_elements(self):
        return self._list1.intersection(self._list2)

if __name__ == '__main__':
    list1 = ["Alice", "Bob", "Charlie"]
    list2 = ["Charlie", "David", "Eve"]
    checker = MembershipChecker(list1, list2)
    common_elements = checker.get_common_elements()
    print(f"Common elements: {common_elements}")