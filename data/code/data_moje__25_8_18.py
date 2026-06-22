def calculate_discounted_price(price: float) -> float:
    return price * 0.6

if __name__ == '__main__':
    result = calculate_discounted_price(200)
    print(result)