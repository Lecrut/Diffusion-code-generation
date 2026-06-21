def contains_target(checklist, member):
    for item in checklist:
        if item == member:
            return True
    return False

if __name__ == '__main__':
    valid_members = ('apple', 'banana', 'cherry')
    sample_member1 = 'banana'
    result1 = contains_target(valid_members, sample_member1)
    print(f"Is {sample_member1} a valid member? {result1}")

    sample_member2 = 'grape'
    result2 = contains_target(valid_members, sample_member2)
    print(f"Is {sample_member2} a valid member? {result2}")