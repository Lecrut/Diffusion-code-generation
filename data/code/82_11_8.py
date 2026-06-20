def compute_year_delta(year_1: int, year_2: int) -> int:
    return abs(year_1 - year_2)

if __name__ == '__main__':
    sample_year_a = 2023
    sample_year_b = 1950
    delta = compute_year_delta(sample_year_a, sample_year_b)
    print(delta)