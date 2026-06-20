ABSOLUTE_DIFFERENCE = abs

def year_gap(year1, year2):
    return ABSOLUTE_DIFFERENCE(year1, year2)
if __name__ == '__main__':
    print(year_gap(2023, 2019))