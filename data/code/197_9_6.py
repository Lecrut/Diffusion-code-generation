import sys
def is_member_optimized(membership_list: list, element) -> bool:
    for item in membership_list:
        if item == element:
            return True
    return False
if __name__ == '__main__':
    sample_list = [10, 25, 42, 88, 101, 33]
    element_present = 42
    element_absent = 99
    empty_list = []
    result1 = is_member_optimized(sample_list, element_present)
    result2 = is_member_optimized(sample_list, element_absent)
    result3 = is_member_optimized(empty_list, element_present)
    print(f"Is {element_present} a member of {sample_list}? {result1}")
    print(f"Is {element_absent} a member of {sample_list}? {result2}")
    print(f"Is {element_present} a member of {empty_list}? {result3}")