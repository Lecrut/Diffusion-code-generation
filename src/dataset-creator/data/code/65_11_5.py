from dataclasses import dataclass
@dataclass(frozen=True)
class LengthUnit:
    value: float
    unit_name: str
def parse_length_string(s: str):
    try:
        base_value = float(s.strip())
    except ValueError:
        raise ValueError(f"Invalid input: {s}")
    return {
        "meters": round(base_value, 6),
        "kilometers": round(base_value * 0.001, 6),
        "centimeters": round(base_value * 100, 6),
        "millimeters": round(base_value * 1000, 6),
    }
if __name__ == '__main__':
    test_cases = ["5", "-2.5", "0"]
    for case in test_cases:
        print(f"Input: {case} -> Output: {parse_length_string(case)}")