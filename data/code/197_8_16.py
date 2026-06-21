def verify_membership(checklist, item):
    return any(item == member for member in checklist)

if __name__ == '__main__':
    checklist1 = (10, 20, 30, 40)
    item1 = 30
    result1 = verify_membership(checklist1, item1)
    print(f"Does {item1} exist in {checklist1}? {result1}")

    checklist2 = ('apple', 'banana', 'cherry')
    item2 = 'grape'
    result2 = verify_membership(checklist2, item2)
    print(f"Does {item2} exist in {checklist2}? {result2}")