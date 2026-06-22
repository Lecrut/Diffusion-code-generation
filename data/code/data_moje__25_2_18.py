def compute_discount_metrics(base_amount, percent_reduction):
    if percent_reduction < 0:
        return 0.0, base_amount
    reduction_value = base_amount * (percent_reduction * 0.01)
    return reduction_value, base_amount - reduction_value

if __name__ == '__main__':
    START_PRICE = 500
    DISCOUNT_PCT = 20
    saved, paid = compute_discount_metrics(START_PRICE, DISCOUNT_PCT)
    print(f"{saved:.2f}")
    print(f"{paid:.2f}")