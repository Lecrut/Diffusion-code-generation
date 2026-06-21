class MembershipChecker:
    def __init__(self, members):
        self._members = set(members)

    def find_common_elements(self, other_list):
        return self._members.intersection(other_list)

if __name__ == '__main__':
    sample_members = ["Alice", "Bob", "Charlie", "David"]
    checker = MembershipChecker(sample_members)
    list1 = ["Bob", "Eve", "Frank"]
    list2 = ["Charlie", "Dave", "Eve"]
    common_elements = checker.find_common_elements(list1 + list2)
    print(f"Common elements: {common_elements}")