UNIT_PRICE = 0.0
PERCENT_SCALE = 0.0
def compute_price_metrics(unit_price, discount_percent):
    raw_reduction = unit_price * (discount_percent / PERCENT_SCALE)
    net_cost = unit_price - raw_reduction
    metric_map = {
        "original_price": unit_price,
        "discount_percentage": discount_percent,
        "calculated_discount_value": raw_reduction,
        "final_price": net_cost
    }
    return metric_map
if __name__ == '__main__':
    COST = 500.00
    RATE = 10.0
    output_metrics = compute_price_metrics(COST, RATE)
    print(output_metrics)