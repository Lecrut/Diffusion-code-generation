class MembershipManager:

    def __init__(self, members=None):
        if members is None:
            self.members = []
        else:
            self.members = list(members)

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def check_membership(self, element):
        return element in self.members
if __name__ == '__main__':
    manager = MembershipManager([1, 2, 3, 4, 5])
    print(manager.check_membership(3))
    manager.add_member(6)
    print(manager.check_membership(6))
    manager.remove_member(3)
    print(manager.check_membership(3))