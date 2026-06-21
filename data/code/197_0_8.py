class Checklist:

    def __init__(self):
        self.members = set()

    def add_member(self, member):
        self.members.add(member)

    def remove_member(self, member):
        self.members.discard(member)

    def has_member(self, member):
        return member in self.members
if __name__ == '__main__':
    checklist = Checklist()
    checklist.add_member('Alice')
    checklist.add_member('Bob')
    print(checklist.has_member('Alice'))
    print(checklist.has_member('Charlie'))
    checklist.remove_member('Alice')
    print(checklist.has_member('Alice'))