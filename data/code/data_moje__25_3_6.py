TIER_MAP = {
    'standard': 0.05,
    'premium': 0.10
}

def compute_final_price(base_amount):
    tier = 'premium' if base_amount > 100 else 'standard'
    rate = TIER_MAP[tier]
    return base_amount * (1 - rate)

if __name__ == '__main__':
    print(compute_final_price(50))
    print(compute_final_price(150))