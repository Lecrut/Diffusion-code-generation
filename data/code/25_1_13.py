def compute_discounted_price(price: float, discount_rate: float = 0.15) -> float:
    return price * (1 - discount_rate)

if __name__ == '__main__':
    price1 = 100
    price2 = 250
    discounted_price1 = compute_discounted_price(price1)
    discounted_price2 = compute_discounted_price(price2)
    print(discounted_price1)
    print(discounted_price2)