class MemberChecklist:

    def __init__(self):
        self.members = set()

    def add_member(self, member):
        self.members.add(member)

    def check_membership(self, member):
        return member in self.members
if __name__ == '__main__':
    checklist = MemberChecklist()
    checklist.add_member('Alice')
    checklist.add_member('Bob')
    print(checklist.check_membership('Alice'))
    print(checklist.check_membership('Charlie'))