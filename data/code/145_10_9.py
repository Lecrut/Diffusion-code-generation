def is_eligible_for_discount(membership_status, purchase_amount):
    return membership_status and purchase_amount >= 100
if __name__ == '__main__':
    print(is_eligible_for_discount(True, 50))
    print(is_eligible_for_discount(False, 200))
    print(is_eligible_for_discount(True, 150))