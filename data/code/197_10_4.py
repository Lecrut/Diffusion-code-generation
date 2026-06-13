def check_membership(individual, membership_criteria):
    for group in membership_criteria:
        if individual in group:
            return True
    return False
if __name__ == '__main__':
    membership_groups = [
        ["Alice", "Bob"],
        ["Charlie", "David", "Eve"],
        ["Frank", "Grace"]
    ]
    individual_to_check = "David"
    is_member = check_membership(individual_to_check, membership_groups)
    print(f"{individual_to_check} is a member: {is_member}")