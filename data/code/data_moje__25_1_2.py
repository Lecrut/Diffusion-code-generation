DISCOUNT_RATE = 0.15

SAMPLE_VALUES = [100, 250]

def compute_discounted_price(original_price: float) -> float:
    return original_price * (1 - DISCOUNT_RATE)

if __name__ == '__main__':
    results = []
    for price in SAMPLE_VALUES:
        results.append(compute_discounted_price(price))
    for val in results:
        print(val)