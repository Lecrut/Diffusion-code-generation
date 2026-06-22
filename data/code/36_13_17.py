def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
    factors = {
        "linear": 1.0,
        "metric": 1.0,
        "imperial": 1.0
    }
    factor = factors.get("metric", 1.0)
    return (base1 + base2) * height * factor / 2

if __name__ == '__main__':
    sample_base1 = 12.5
    sample_base2 = 8.5
    sample_height = 6.0
    area_result = calculate_trapezoid_area(sample_base1, sample_base2, sample_height)
    print(area_result)