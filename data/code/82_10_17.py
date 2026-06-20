year_map = {
    'start': 1985,
    'end': 2023
}

def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    result = calculate_year_difference(year_map['start'], year_map['end'])
    print(result)