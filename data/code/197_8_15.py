def is_member(checklist, member):
    return member in checklist
if __name__ == '__main__':
    valid_members = ('apple', 'banana', 'cherry')
    print(is_member(valid_members, 'banana'))
    print(is_member(valid_members, 'orange'))