def is_member(checklist, item):
    return item in checklist

if __name__ == '__main__':
    valid_members = (1, 2, 3, 4, 5)
    item_to_check = 3
    result = is_member(valid_members, item_to_check)
    print(f"Is {item_to_check} a member of the checklist? {result}")
    
    item_to_check = 6
    result = is_member(valid_members, item_to_check)
    print(f"Is {item_to_check} a member of the checklist? {result}")