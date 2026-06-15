class GroupManager:
    def __init__(self):
        self.memberships = {}
    def add_membership(self, entity, group):
        if entity not in self.memberships:
            self.memberships[entity] = set()
        self.memberships[entity].add(group)
    def remove_membership(self, entity, group):
        if entity in self.memberships and group in self.memberships[entity]:
            self.memberships[entity].remove(group)
            if not self.memberships[entity]:
                del self.memberships[entity]
    def has_membership(self, entity, group):
        if entity in self.memberships:
            return group in self.memberships[entity]
        return False
    def get_all_memberships(self):
        return self.memberships
if __name__ == '__main__':
    manager = GroupManager()
    manager.add_membership("Alice", "Admins")
    manager.add_membership("Alice", "Developers")
    manager.add_membership("Bob", "Developers")
    manager.add_membership("Charlie", "Admins")
    manager.add_membership("Alice", "Admins")
    print("--- Initial Memberships ---")
    print(manager.get_all_memberships())
    print("\n--- Checking Membership ---")
    print(f"Alice is in Admins: {manager.has_membership('Alice', 'Admins')}")
    print(f"Bob is in Admins: {manager.has_membership('Bob', 'Admins')}")
    print(f"David is in Developers: {manager.has_membership('David', 'Developers')}")
    print("\n--- Removing Membership ---")
    manager.remove_membership("Alice", "Developers")
    print(f"Alice is in Developers after removal: {manager.has_membership('Alice', 'Developers')}")
    print(manager.get_all_memberships())
    manager.remove_membership("Bob", "Developers")
    print(manager.get_all_memberships())
    manager.remove_membership("Eve", "NonExistentGroup")
    print(manager.get_all_memberships())