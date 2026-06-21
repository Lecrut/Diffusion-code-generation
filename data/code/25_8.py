def calculate_discounted_price(price: float) -> float:
    return price * 0.6

if __name__ == '__main__':
    initial_price: float = 200.0
    final_price: float = calculate_discounted_price(initial_price)
    print(final_price)