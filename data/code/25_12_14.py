def compute_discount_info(price_before, pct_off):
    derived_discount = price_before * pct_off / 100.0
    price_after = price_before - derived_discount
    return {
        "original_price": price_before,
        "discount_percentage": pct_off,
        "calculated_discount_value": derived_discount,
        "final_price": price_after
    }

if __name__ == '__main__':
    demo_price = 150.0
    demo_discount = 10.0
    result_dict = compute_discount_info(demo_price, demo_discount)
    print(result_dict)