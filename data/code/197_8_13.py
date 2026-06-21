def is_member(checklist, item):
    return item in checklist

if __name__ == '__main__':
    valid_members = ('apple', 'banana', 'cherry')
    sample_item = 'banana'
    print(is_member(valid_members, sample_item))