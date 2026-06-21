def validate_price(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Price must be numeric")
    if amount < 0:
        raise ValueError("Price cannot be negative")
    return True

def compute_final_tiered_price(price):
    validate_price(price)
    rate = 0.1 if price > 100 else 0.05
    discounted_amount = price * (1 - rate)
    return discounted_amount

if __name__ == '__main__':
    print(compute_final_tiered_price(50))
    print(compute_final_tiered_price(150))