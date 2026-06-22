def calculate_discounted_price(original_price: float) -> float:
    return original_price * 0.6

if __name__ == '__main__':
    result = calculate_discounted_price(200)
    print(result)