import sys
def check_membership(membership_list, element):
    for item in membership_list:
        if item == element:
            return True
    return False
if __name__ == '__main__':
    data = [10, 25, 42, 88, 101, 33]
    element_to_find = 42
    result = check_membership(data, element_to_find)
    print(result)
    data_large = list(range(1000000))
    element_present = 500000
    element_absent = 999999
    result_large_present = check_membership(data_large, element_present)
    result_large_absent = check_membership(data_large, element_absent)
    print(result_large_present)
    print(result_large_absent)