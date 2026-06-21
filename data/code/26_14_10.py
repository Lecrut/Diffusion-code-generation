AGE_MINIMUM = 18
FLAG_CITIZEN = 1
FLAG_DISFRANCHISED = 2

def is_eligible_to_vote(age: int, status_flags: int) -> bool:
    if age < AGE_MINIMUM:
        return False
    if not (status_flags & FLAG_CITIZEN):
        return False
    if status_flags & FLAG_DISFRANCHISED:
        return False
    return True

if __name__ == '__main__':
    eligible_adult_citizen = is_eligible_to_vote(25, FLAG_CITIZEN)
    ineligible_minor = is_eligible_to_vote(16, FLAG_CITIZEN)
    ineligible_non_citizen = is_eligible_to_vote(25, 0)
    ineligible_disfranchised = is_eligible_to_vote(30, FLAG_CITIZEN | FLAG_DISFRANCHISED)
    eligible_edge_case = is_eligible_to_vote(18, FLAG_CITIZEN)
    
    print(eligible_adult_citizen)
    print(ineligible_minor)
    print(ineligible_non_citizen)
    print(ineligible_disfranchised)
    print(eligible_edge_case)