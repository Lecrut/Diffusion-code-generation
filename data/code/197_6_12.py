class MembershipManager:

    def __init__(self, initial_members=None):
        self.members = [] if initial_members is None else list(initial_members)

    def add_member(self, member):
        if not isinstance(member, (int, str)):
            raise ValueError('Member must be an integer or string')
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            raise ValueError(f'Member {member} not found')

    def check_membership(self, element):
        if not isinstance(element, (int, str)):
            raise ValueError('Element must be an integer or string')
        return element in self.members
if __name__ == '__main__':
    manager = MembershipManager([1, 2, 3, 4, 5])
    print(manager.check_membership(3))
    manager.add_member('a')
    print(manager.check_membership('a'))
    manager.remove_member(3)
    print(manager.check_membership(3))