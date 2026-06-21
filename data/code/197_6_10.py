class MembershipManager:

    def __init__(self):
        self.members = set()

    def add_member(self, member):
        self.members.add(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def is_member(self, member):
        return member in self.members
if __name__ == '__main__':
    manager = MembershipManager()
    manager.add_member('Alice')
    manager.add_member('Bob')
    print(manager.is_member('Alice'))
    print(manager.is_member('Charlie'))
    manager.remove_member('Alice')
    print(manager.is_member('Alice'))