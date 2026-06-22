WEIGHT_TOLERANCE_THRESHOLD = 0.0
SIGN_PRECISION_MULTIPLIER = 100

def compute_weight_delta(first_mass, second_mass):
    raw_delta = first_mass - second_mass
    sign_indicator = 1 if raw_delta > WEIGHT_TOLERANCE_THRESHOLD else (-1 if raw_delta < -WEIGHT_TOLERANCE_THRESHOLD else 0)
    scaled_value = raw_delta * SIGN_PRECISION_MULTIPLIER
    rounded_value = round(scaled_value)
    normalized_delta = rounded_value / SIGN_PRECISION_MULTIPLIER
    if sign_indicator == 0:
        return 0.0
    if sign_indicator < 0:
        return normalized_delta * -1
    return normalized_delta

if __name__ == '__main__':
    mass_start = 120.75
    mass_end = 118.30
    delta_result = compute_weight_delta(mass_start, mass_end)
    print(delta_result)