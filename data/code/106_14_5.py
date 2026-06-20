from datetime import datetime

def calculate_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_years = {
        'year1': 2023,
        'year2': 1998
    }
    
    difference = calculate_year_difference(sample_years['year1'], sample_years['year2'])
    print(f"The absolute difference between {sample_years['year1']} and {sample_years['year2']} is: {difference}")