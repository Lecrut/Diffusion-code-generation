def is_eligible_for_discount(is_member, purchase_amount):
    return is_member and purchase_amount >= 100
if __name__ == '__main__':
    print(is_eligible_for_discount(True, 95))
    print(is_eligible_for_discount(False, 200))
    print(is_eligible_for_discount(True, 150))