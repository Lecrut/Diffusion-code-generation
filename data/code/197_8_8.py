def is_member(checklist, member):
    return member in checklist

if __name__ == '__main__':
    valid_members = ('apple', 'banana', 'cherry')
    sample_member = 'banana'
    print(is_member(valid_members, sample_member))