from datetime import datetime

def calculate_year_difference(year1_str: str, year2_str: str) -> int:
    try:
        year1 = int(year1_str)
        year2 = int(year2_str)
        return abs(year1 - year2)
    except ValueError:
        raise ValueError('Error: Please enter valid integer years.')
if __name__ == '__main__':
    year1_str = '2023'
    year2_str = '1998'
    try:
        difference = calculate_year_difference(year1_str, year2_str)
        print(f'The absolute difference between {year1_str} and {year2_str} is: {difference}')
    except ValueError as e:
        print(e)