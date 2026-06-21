class MembershipChecker:
    def __init__(self, list1, list2):
        self._members = set(list1) & set(list2)

    def get_common_members(self):
        return self._members

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob", "Charlie"]
    sample_list2 = ["Bob", "David", "Eve"]
    checker = MembershipChecker(sample_list1, sample_list2)
    print(f"Common members: {checker.get_common_members()}")