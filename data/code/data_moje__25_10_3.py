def compute_discount(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    sample_price = 100.0
    sample_discount_rate = 0.15
    discount_amount, final_price = compute_discount(sample_price, sample_discount_rate)
    print(f"Discount Amount: {discount_amount}")
    print(f"Final Price: {final_price}")