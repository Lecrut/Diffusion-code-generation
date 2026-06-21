def is_member(checklist, item):
    for member in checklist:
        if member == item:
            return True
    return False

if __name__ == '__main__':
    sample_checklist = ('apple', 'banana', 'cherry')
    sample_item = 'banana'
    print(is_member(sample_checklist, sample_item))