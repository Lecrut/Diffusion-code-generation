MULTIPLIER = 0.95

def compute_discounted_prices(prices, discount_rate):
    factor = 1.0 - discount_rate
    return (p * factor for p in prices)

if __name__ == '__main__':
    hard_coded = [100, 200, 300]
    results = list(compute_discounted_prices(hard_coded, 0.05))
    print(results)