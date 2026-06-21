class MembershipManager:

    def __init__(self, members):
        self.members = set(members)

    def is_member(self, element):
        return element in self.members
if __name__ == '__main__':
    sample_members = [1, 2, 3, 4, 5]
    manager = MembershipManager(sample_members)
    print(manager.is_member(3))
    print(manager.is_member(6))