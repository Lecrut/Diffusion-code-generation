BASE_SAMPLE = 5
EXPONENT_SAMPLE = 4

def compute_power(base_value, exponent_value):
    return base_value ** exponent_value

if __name__ == "__main__":
    result = compute_power(BASE_SAMPLE, EXPONENT_SAMPLE)
    print(result)