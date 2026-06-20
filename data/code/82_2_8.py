def calculate_year_difference(year1: str, year2: str) -> int:
    years = {'year1': int(year1), 'year2': int(year2)}
    return abs(years['year1'] - years['year2'])

if __name__ == '__main__':
    difference = calculate_year_difference('2023', '1990')
    print(f"The difference between 2023 and 1990 is: {difference}")