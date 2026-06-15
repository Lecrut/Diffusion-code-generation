import sys
def check_membership(membership_list, element):
    for item in membership_list:
        if item == element:
            return True
    return False
if __name__ == '__main__':
    data = [10, 25, 33, 42, 55, 67, 89, 101]
    element_present = 42
    element_absent = 99
    result_present = check_membership(data, element_present)
    result_absent = check_membership(data, element_absent)
    print(f"Is {element_present} in the list? {result_present}")
    print(f"Is {element_absent} in the list? {result_absent}")