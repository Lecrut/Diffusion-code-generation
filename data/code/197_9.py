import sys
def check_membership(membership_list, element):
    for item in membership_list:
        if item == element:
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    element_present = 10
    element_absent = 99
    result1 = check_membership(sample_list, element_present)
    result2 = check_membership(sample_list, element_absent)
    print(f"Membership check for {element_present}: {result1}")
    print(f"Membership check for {element_absent}: {result2}")