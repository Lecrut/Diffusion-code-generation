from typing import List

def check_membership(membership_list: List[int], element: int) -> bool:
    return element in membership_list

if __name__ == '__main__':
    sample_ids = [10, 25, 42, 88, 101, 33]
    id_to_check_present = 42
    id_to_check_absent = 99
    result_present = check_membership(sample_ids, id_to_check_present)
    result_absent = check_membership(sample_ids, id_to_check_absent)
    print(f"ID {id_to_check_present} is in the list: {result_present}")
    print(f"ID {id_to_check_absent} is in the list: {result_absent}")