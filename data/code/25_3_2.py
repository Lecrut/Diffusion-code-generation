DISCOUNT_THRESHOLD = 100
HIGH_DISCOUNT_RATE = 0.10
LOW_DISCOUNT_RATE = 0.05

def get_tiered_discounted_price(amount):
    is_high_tier = amount > DISCOUNT_THRESHOLD
    applicable_rate = HIGH_DISCOUNT_RATE if is_high_tier else LOW_DISCOUNT_RATE
    discount_amount = amount * applicable_rate
    final_price = amount - discount_amount
    return final_price

if __name__ == '__main__':
    sample_input_low = 50
    sample_input_high = 150
    result_low = get_tiered_discounted_price(sample_input_low)
    result_high = get_tiered_discounted_price(sample_input_high)
    print(result_low)
    print(result_high)