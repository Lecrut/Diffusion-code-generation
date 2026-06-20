def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    current_year = 2023
    birth_year = 1985
    age = calculate_year_difference(current_year, birth_year)
    print(age)