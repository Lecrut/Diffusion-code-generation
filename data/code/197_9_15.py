MEMBERSHIP_CHECKLIST = {1, 5, 10, 15, 20}

def is_member(element: int) -> bool:
    return element in MEMBERSHIP_CHECKLIST

if __name__ == '__main__':
    sample_id_present = 10
    sample_id_absent = 99
    result_present = is_member(sample_id_present)
    result_absent = is_member(sample_id_absent)
    print(f"Membership check for {sample_id_present}: {result_present}")
    print(f"Membership check for {sample_id_absent}: {result_absent}")