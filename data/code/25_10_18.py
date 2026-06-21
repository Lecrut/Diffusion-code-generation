def calculate_discounted_price(price: float, discount_rate: float) -> tuple:
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    sample_price = 100.0
    sample_discount_rate = 0.2
    amount, final = calculate_discounted_price(sample_price, sample_discount_rate)
    print(f"{amount}")
    print(f"{final}")