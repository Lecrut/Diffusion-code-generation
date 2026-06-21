def verify_checklist_membership(member, valid_members):
    return member in valid_members

if __name__ == '__main__':
    sample_member = 'apple'
    sample_valid_members = ('apple', 'banana', 'cherry')
    print(verify_checklist_membership(sample_member, sample_valid_members))