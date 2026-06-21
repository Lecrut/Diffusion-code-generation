class ChecklistMember:

    def __init__(self, members):
        self.members = set(members)

    def is_member(self, individual):
        return individual in self.members
if __name__ == '__main__':
    checklist = ChecklistMember(['Alice', 'Bob', 'Charlie'])
    print(checklist.is_member('Bob'))
    print(checklist.is_member('Zoe'))