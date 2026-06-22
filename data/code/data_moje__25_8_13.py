def calculate_final_price(price: float) -> float:
    return price * (1 - 0.4)

if __name__ == '__main__':
    result = calculate_final_price(200)
    print(result)