class GroupMembershipManager:
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
if __name__ == '__main__':
    manager = GroupMembershipManager()
    manager.add_membership("Alice", "Admins")
    manager.add_membership("Alice", "Developers")
    manager.add_membership("Bob", "Developers")
    manager.add_membership("Charlie", "Admins")
    print(f"Alice has Admins: {manager.has_membership('Alice', 'Admins')}")
    print(f"Bob has Admins: {manager.has_membership('Bob', 'Admins')}")
    print(f"Charlie has Developers: {manager.has_membership('Charlie', 'Developers')}")
    print(f"David has Admins: {manager.has_membership('David', 'Admins')}")
    manager.remove_membership("Alice", "Developers")
    print(f"Alice has Developers after removal: {manager.has_membership('Alice', 'Developers')}")
    manager.remove_membership("Bob", "Developers")
    print(f"Bob has Developers after removal: {manager.has_membership('Bob', 'Developers')}")
    manager.remove_membership("Alice", "Admins")
    print(f"Alice has Admins after removal: {manager.has_membership('Alice', 'Admins')}")
    manager.remove_membership("Charlie", "Admins")
    print(f"Charlie has Admins after removal: {manager.has_membership('Charlie', 'Admins')}")