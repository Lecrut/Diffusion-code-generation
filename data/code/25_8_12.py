def calculate_final_price(price: float, discount_rate: float) -> float:
    return price * (1 - discount_rate)

if __name__ == '__main__':
    input_price: float = 200
    discount: float = 0.40
    final_price: float = calculate_final_price(input_price, discount)
    print(final_price)