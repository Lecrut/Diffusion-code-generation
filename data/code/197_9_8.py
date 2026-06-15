import sys
def check_membership(membership_list, element):
    for item in membership_list:
        if item == element:
            return True
    return False
if __name__ == '__main__':
    data = [10, 25, 33, 48, 51, 67, 89]
    element_present = 51
    element_absent = 99
    result1 = check_membership(data, element_present)
    result2 = check_membership(data, element_absent)
    print(f"Is {element_present} in {data}? {result1}")
    print(f"Is {element_absent} in {data}? {result2}")