def apply_price_adjustment(base_amount, reduction_rate):
    reduction_amount = base_amount * (reduction_rate / 100.0)
    final_cost = base_amount - reduction_amount
    result_data = {
        "original_price": base_amount,
        "discount_percentage": reduction_rate,
        "calculated_discount_value": reduction_amount,
        "final_price": final_cost
    }
    return result_data

if __name__ == '__main__':
    SAMPLE_BASE = 250.00
    SAMPLE_RATE = 15.0
    output = apply_price_adjustment(SAMPLE_BASE, SAMPLE_RATE)
    print(output)