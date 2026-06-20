def calculate_year_difference(year1: str, year2: str) -> int:
    try:
        return abs(int(year1) - int(year2))
    except ValueError:
        raise ValueError("Both inputs must be valid integers representing years.")

if __name__ == '__main__':
    print(calculate_year_difference('2023', '1990'))