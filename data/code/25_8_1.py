def calculate_discounted_price(base_price: float) -> float:
    return base_price * 0.6

if __name__ == '__main__':
    initial_cost: float = 200
    final_price: float = calculate_discounted_price(initial_cost)
    print(final_price)