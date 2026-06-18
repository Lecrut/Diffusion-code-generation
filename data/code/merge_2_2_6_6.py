import math
def is_positively_signed(value: float) -> bool:
    return value > 1e-6 and not (math.isnan(value) or math.isinf(value))
if __name__ == '__main__':
    test_cases = [0.0, -1e-9, 1e-9, float('nan'), float('-inf'), float('inf')]
    for val in test_cases:
        print(f"Value {val}: is_positively_signed={is_positively_signed(val)}")