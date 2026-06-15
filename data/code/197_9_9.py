def is_member(membership_list, element):
    for item in membership_list:
        if item == element:
            return True
    return False
if __name__ == '__main__':
    members = [1, 5, 10, 15, 20]
    element_to_check_present = 10
    element_to_check_absent = 99
    result1 = is_member(members, element_to_check_present)
    result2 = is_member(members, element_to_check_absent)
    print(f"Is {element_to_check_present} a member? {result1}")
    print(f"Is {element_to_check_absent} a member? {result2}")