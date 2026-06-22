DISCOUNT_RATES = {
    "standard": 0.10,
    "premium": 0.20,
    "bulk": 0.05
}

ITEM_PRICE = 75.50
TARGET_DISCOUNT_KEY = "standard"

def calculate_final_cost(price, discount_rate):
    discount_value = price * discount_rate
    return price - discount_value

if __name__ == '__main__':
    rate = DISCOUNT_RATES[TARGET_DISCOUNT_KEY]
    total = calculate_final_cost(ITEM_PRICE, rate)
    print(total)