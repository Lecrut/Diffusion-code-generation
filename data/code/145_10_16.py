def is_eligible_for_discount(membership_status, purchase_amount):
    if not isinstance(membership_status, bool) or not isinstance(purchase_amount, (int, float)):
        raise ValueError("Invalid input: membership_status must be a boolean and purchase_amount must be a number.")
    
    return (membership_status and purchase_amount > 100) or (not membership_status and purchase_amount > 200)

if __name__ == '__main__':
    print("--- Testing Discount Eligibility ---")
    member = True
    spent = 95
    result_member_spent = is_eligible_for_discount(member, spent)
    print(f"Test Case 1 (member={member}, spent={spent}): Result = {result_member_spent}")
    
    non_member = False
    spent = 205
    result_non_member_spent = is_eligible_for_discount(non_member, spent)
    print(f"Test Case 2 (non-member={non_member}, spent={spent}): Result = {result_non_member_spent}")