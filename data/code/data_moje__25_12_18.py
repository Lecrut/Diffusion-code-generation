DISCOUNT_PERCENT_DIVISOR = 100

def get_price_breakdown(initial_cost, percent_off):
    reduction_amount = initial_cost * (percent_off / DISCOUNT_PERCENT_DIVISOR)
    final_cost = initial_cost - reduction_amount
    return {
        "original_price": initial_cost,
        "discount_percentage": percent_off,
        "calculated_discount_value": reduction_amount,
        "final_price": final_cost
    }

if __name__ == '__main__':
    TEST_COST = 85.50
    TEST_PERCENT = 25
    data = get_price_breakdown(TEST_COST, TEST_PERCENT)
    print(data)