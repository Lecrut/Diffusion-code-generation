DISCOUNT_CONFIG = {
    'rate_divisor': 100,
    'default_discount': 30,
    'sample_price': 99.99
}

def compute_pricing_metrics(price_val, disc_val):
    multiplier = disc_val / DISCOUNT_CONFIG['rate_divisor']
    saved_amt = price_val * multiplier
    net_total = price_val - saved_amt
    return (price_val, saved_amt, net_total)

if __name__ == '__main__':
    base_cost = DISCOUNT_CONFIG['sample_price']
    cut_pct = DISCOUNT_CONFIG['default_discount']
    output_tuple = compute_pricing_metrics(base_cost, cut_pct)
    print(output_tuple)