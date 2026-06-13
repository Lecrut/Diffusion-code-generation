def check_membership(individual, membership_criteria):
    for group in membership_criteria:
        if individual in group:
            return True
    return False
if __name__ == '__main__':
    membership_data = [
        ["Alice", "GroupA"],
        ["Bob", "GroupB"],
        ["Charlie", "GroupA"],
        ["David", "GroupC"]
    ]
    individual_to_check = "Alice"
    is_member = check_membership(individual_to_check, membership_data)
    print(f"{individual_to_check} is a member: {is_member}")
    individual_to_check = "Eve"
    is_member = check_membership(individual_to_check, membership_data)
    print(f"{individual_to_check} is a member: {is_member}")