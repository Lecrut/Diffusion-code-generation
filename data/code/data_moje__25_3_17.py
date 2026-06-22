def calculate_price(original_price):
    if original_price > 100:
        return original_price * 0.9
    return original_price * 0.95

if __name__ == '__main__':
    print(calculate_price(50))
    print(calculate_price(150))