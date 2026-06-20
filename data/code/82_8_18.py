def find_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both arguments must be integers representing years.")
    
    return abs(year1 - year2)

if __name__ == '__main__':
    year_a = 2023
    year_b = 1998
    difference = find_year_difference(year_a, year_b)
    print(difference)