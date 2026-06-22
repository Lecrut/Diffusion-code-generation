def _validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Price must be numeric")
    if value < 0:
        raise ValueError("Price cannot be negative")
    return True

def _validate_discount(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Discount must be numeric")
    if value < 0 or value > 100:
        raise ValueError("Discount must be between 0 and 100")
    return True

def compute_pricing_metrics(original_price, discount_percent):
    _validate_price(original_price)
    _validate_discount(discount_percent)
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return (original_price, discount_amount, final_price)

if __name__ == '__main__':
    sample_price = 99.99
    sample_discount = 30
    metrics = compute_pricing_metrics(sample_price, sample_discount)
    print(metrics)