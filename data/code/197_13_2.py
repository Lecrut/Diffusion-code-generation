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
if __name__ == '__main__':
    manager = GroupManager()
    manager.add_membership("Alice", "Admins")
    manager.add_membership("Alice", "Developers")
    manager.add_membership("Bob", "Developers")
    manager.add_membership("Charlie", "Admins")
    print(f"Alice is in Admins: {manager.has_membership('Alice', 'Admins')}")
    print(f"Bob is in Admins: {manager.has_membership('Bob', 'Admins')}")
    print(f"Charlie is in Developers: {manager.has_membership('Charlie', 'Developers')}")
    print(f"David is in Admins: {manager.has_membership('David', 'Admins')}")
    manager.remove_membership("Alice", "Developers")
    print(f"Alice is in Developers after removal: {manager.has_membership('Alice', 'Developers')}")
    manager.remove_membership("Bob", "Developers")
    print(f"Bob is in Developers after removal: {manager.has_membership('Bob', 'Developers')}")
    manager.remove_membership("Alice", "Admins")
    print(f"Alice is in Admins after removal: {manager.has_membership('Alice', 'Admins')}")
    print(f"Alice's current groups: {manager.memberships.get('Alice')}")
    print(f"Bob's current groups: {manager.memberships.get('Bob')}")