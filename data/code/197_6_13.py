class MembershipManager:

    def __init__(self):
        self.members = set()

    def add_member(self, member):
        if not isinstance(member, str):
            raise ValueError('Member must be a string.')
        self.members.add(member)

    def check_membership(self, member):
        return member in self.members
if __name__ == '__main__':
    manager = MembershipManager()
    manager.add_member('Alice')
    manager.add_member('Bob')
    print(manager.check_membership('Alice'))
    print(manager.check_membership('Charlie'))