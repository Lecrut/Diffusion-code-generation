discount_settings = {
    "sample_price": 150.0,
    "sample_discount_rate": 0.25
}

def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    price = discount_settings["sample_price"]
    rate = discount_settings["sample_discount_rate"]
    result = calculate_discount(price, rate)
    print(result[0])
    print(result[1])