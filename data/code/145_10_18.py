def is_eligible_for_discount(is_member, purchase_amount):
    return is_member and (purchase_amount >= 100 or purchase_amount < 50)
if __name__ == '__main__':
    print(is_eligible_for_discount(True, 90))
    print(is_eligible_for_discount(False, 150))
    print(is_eligible_for_discount(True, 120))