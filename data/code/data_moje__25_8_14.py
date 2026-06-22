def calculate_final_price(price: float) -> float:
    return price * 0.6

if __name__ == '__main__':
    original_price: float = 200.0
    final_price: float = calculate_final_price(original_price)
    print(final_price)