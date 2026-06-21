class MembershipManager:

    def __init__(self):
        self.members = []

    def add_member(self, member):
        if isinstance(member, str) and member not in self.members:
            self.members.append(member)
            return True
        return False

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            return True
        return False

    def check_membership(self, member):
        return member in self.members
if __name__ == '__main__':
    manager = MembershipManager()
    manager.add_member('Alice')
    manager.add_member('Bob')
    print(manager.check_membership('Alice'))
    print(manager.check_membership('Charlie'))