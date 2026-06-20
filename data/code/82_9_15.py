def validate_year(year):
    try:
        year = int(year)
        if year < 0:
            raise ValueError("Year must be non-negative")
        return year
    except ValueError as e:
        print(f"Error: {e}")
        return None

def calculate_difference(year1, year2):
    if year1 is not None and year2 is not None:
        return abs(year1 - year2)
    else:
        return None

if __name__ == '__main__':
    year1 = validate_year(2024)
    year2 = validate_year(1999)
    difference = calculate_difference(year1, year2)
    print(difference)