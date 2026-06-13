def check_membership(individual, membership_criteria):
    for group_id, criteria in membership_criteria.items():
        if individual in criteria:
            return True
    return False
if __name__ == '__main__':
    membership_data = {
        "GroupA": ["Alice", "Bob", "Charlie"],
        "GroupB": ["Bob", "David", "Eve"],
        "GroupC": ["Alice", "Frank"]
    }
    individual_to_check = "Bob"
    is_member = check_membership(individual_to_check, membership_data)
    print(f"{individual_to_check} is a member: {is_member}")
    individual_to_check_2 = "Zoe"
    is_member_2 = check_membership(individual_to_check_2, membership_data)
    print(f"{individual_to_check_2} is a member: {is_member_2}")