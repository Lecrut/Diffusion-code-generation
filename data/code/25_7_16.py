def apply_single_discount(value, rate):
    reduction = value * rate
    return value - reduction

def compute_discounted_prices(prices, discount_rate):
    multiplier = 1 - discount_rate
    results = []
    for current_price in prices:
        discounted_price = apply_single_discount(current_price, discount_rate)
        results.append(discounted_price)
    return results

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    discount_percentage = 0.05
    output_list = compute_discounted_prices(sample_values, discount_percentage)
    print(output_list)