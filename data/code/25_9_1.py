def compute_discounted_price(original_amount: float, discount_rate: float) -> float:
    if original_amount < 0:
        raise ValueError("Original amount must be non-negative")
    if discount_rate < 0:
        raise ValueError("Discount rate cannot be negative")
    if discount_rate > 100:
        raise ValueError("Discount rate cannot exceed 100 percent")
    reduction_factor = 1.0 - (discount_rate / 100.0)
    return original_amount * reduction_factor

if __name__ == '__main__':
    test_amount = 200.0
    test_rate = 15.0
    computed_result = compute_discounted_price(test_amount, test_rate)
    print(computed_result)
    edge_case_result = compute_discounted_price(50.0, 0.0)
    print(edge_case_result)
    full_discount_result = compute_discounted_price(100.0, 100.0)
    print(full_discount_result)