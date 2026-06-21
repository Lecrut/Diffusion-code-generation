def is_member(checklist, member):
    return member in checklist

if __name__ == '__main__':
    valid_members = ('apple', 'banana', 'cherry', 'date')
    sample_members = ['apple', 'orange', 'banana', 'grape']

    for member in sample_members:
        result = is_member(valid_members, member)
        print(f"Is '{member}' a valid member? {result}")