def check_membership(membership_list: list[int], element: int) -> bool:
    return element in membership_list

if __name__ == '__main__':
    sample_ids = [1, 5, 10, 15, 20]
    id_present = 10
    id_absent = 99
    result1 = check_membership(sample_ids, id_present)
    result2 = check_membership(sample_ids, id_absent)
    print(f"ID {id_present} is present: {result1}")
    print(f"ID {id_absent} is present: {result2}")