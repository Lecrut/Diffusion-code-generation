class MembershipChecker:
    CHECKLIST_MEMBERS = {1, 5, 10, 15, 20}

    @staticmethod
    def is_member(element: int) -> bool:
        return element in MembershipChecker.CHECKLIST_MEMBERS

if __name__ == '__main__':
    sample_id_present = 10
    sample_id_absent = 99
    result1 = MembershipChecker.is_member(sample_id_present)
    result2 = MembershipChecker.is_member(sample_id_absent)
    print(f"ID {sample_id_present} is in the checklist: {result1}")
    print(f"ID {sample_id_absent} is in the checklist: {result2}")