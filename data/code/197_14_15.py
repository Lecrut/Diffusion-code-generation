class SubsetChecker:
    def __init__(self):
        self.master_list = set()
    
    def update_master_list(self, items):
        self.master_list.update(items)
    
    def is_subset(self, subset_items):
        return subset_items.issubset(self.master_list)

if __name__ == '__main__':
    checker = SubsetChecker()
    group_a_members = {101, 102, 103, 104, 105}
    group_b_members = {104, 105, 106, 107, 108}
    
    checker.update_master_list(group_a_members)
    checker.update_master_list(group_b_members)
    
    print(f"Is group A a subset of the master list? {checker.is_subset(group_a_members)}")
    print(f"Is group B a subset of the master list? {checker.is_subset(group_b_members)}")
    print(f"Is an empty set a subset of the master list? {checker.is_subset(set())}")