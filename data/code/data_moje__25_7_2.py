def compute_discounted_prices():
    values = [100, 200, 300]
    discount_rate = 0.05
    return [v * (1 - discount_rate) for v in values]

if __name__ == '__main__':
    print(compute_discounted_prices())