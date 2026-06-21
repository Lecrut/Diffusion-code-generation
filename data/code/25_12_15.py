def compute_discount_metrics(base_cost, percent_reduction):
    if base_cost < 0:
        raise ValueError("Base cost cannot be negative")
    if percent_reduction < 0 or percent_reduction > 100:
        raise ValueError("Percent reduction must be between 0 and 100")
    
    cut_amount = base_cost * percent_reduction * 0.01
    net_total = base_cost - cut_amount
    
    return {
        "original_price": base_cost,
        "discount_percentage": percent_reduction,
        "calculated_discount_value": cut_amount,
        "final_price": net_total
    }

if __name__ == '__main__':
    PRICE_A = 450.0
    RATE_A = 30.0
    data = compute_discount_metrics(PRICE_A, RATE_A)
    print(data)