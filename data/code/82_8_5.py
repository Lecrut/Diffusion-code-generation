def find_year_difference(year1, year2):
    if not (isinstance(year1, int) and isinstance(year2, int)):
        raise ValueError("Both inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    print(find_year_difference(2023, 1998))
    print(find_year_difference(2020, 1995))
    print(find_year_difference(2023, 1990))