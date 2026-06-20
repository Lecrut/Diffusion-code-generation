def calculate_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_years = {
        'year1': 2024,
        'year2': 1999
    }
    try:
        difference = calculate_year_difference(sample_years['year1'], sample_years['year2'])
        print(difference)
    except ValueError as e:
        print(e)