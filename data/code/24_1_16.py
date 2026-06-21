def check_divisibility_by_n(year, divisor):
    return year % divisor == 0

def determine_leap_year(year):
    div_400_rules = {
        400: check_divisibility_by_n(year, 400)
    }
    if div_400_rules[400]:
        return True
    
    div_100_rules = {
        100: check_divisibility_by_n(year, 100)
    }
    if div_100_rules[100]:
        return False
    
    div_4_rules = {
        4: check_divisibility_by_n(year, 4)
    }
    return div_4_rules[4]

if __name__ == '__main__':
    sample_years = [2000, 1900, 2024]
    for test_year in sample_years:
        print(determine_leap_year(test_year))