PERCENT_BASE = 100

def compute_discount_details(base_price, pct_off):
    raw_multiplier = pct_off / PERCENT_BASE
    saved_amount = base_price * raw_multiplier
    net_cost = base_price - saved_amount
    return {
        "original_price": base_price,
        "discount_percentage": pct_off,
        "calculated_discount_value": saved_amount,
        "final_price": net_cost
    }

if __name__ == '__main__':
    TEST_PRICE = 200.0
    TEST_PCT = 10.0
    data = compute_discount_details(TEST_PRICE, TEST_PCT)
    print(data)