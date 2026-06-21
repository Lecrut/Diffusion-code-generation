class MembershipChecker:
    def __init__(self):
        self.master_list = set()

    def update_master_list(self, new_members):
        for member in new_members:
            self.master_list.add(member)

    def is_subset(self, subset_list):
        return subset_list.issubset(self.master_list)

if __name__ == '__main__':
    checker = MembershipChecker()
    group_a_members = {101, 102, 103, 104, 105}
    group_b_members = {104, 105, 106, 107, 108}
    checker.update_master_list(group_a_members)
    checker.update_master_list(group_b_members)
    print(f"Is group A a subset of the master list? {checker.is_subset(group_a_members)}")
    print(f"Is group B a subset of the master list? {checker.is_subset(group_b_members)}")