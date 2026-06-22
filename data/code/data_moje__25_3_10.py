TIER_THRESHOLD = 100
HIGH_TIER_MULTIPLIER = 0.9
LOW_TIER_MULTIPLIER = 0.95

def get_discounted_price(price):
    if price > TIER_THRESHOLD:
        return price * HIGH_TIER_MULTIPLIER
    return price * LOW_TIER_MULTIPLIER

if __name__ == '__main__':
    test_values = [50, 150]
    for val in test_values:
        print(get_discounted_price(val))