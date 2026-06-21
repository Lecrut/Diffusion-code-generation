class MembershipManager:

    def __init__(self):
        self.members = []

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def check_membership(self, element):
        return element in self.members
if __name__ == '__main__':
    manager = MembershipManager()
    manager.add_member(3)
    print(manager.check_membership(3))
    print(manager.check_membership(4))
    manager.remove_member(3)
    print(manager.check_membership(3))