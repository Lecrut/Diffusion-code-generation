def calculate_discounted_price(base_price: float, discount_rate: float) -> float:
    return base_price * (1.0 - discount_rate)

if __name__ == '__main__':
    initial_price: float = 200
    discount_percent: float = 0.4
    final_price: float = calculate_discounted_price(initial_price, discount_percent)
    print(final_price)