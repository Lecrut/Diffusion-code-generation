def is_leap(year):
    year_val = year
    bitwise_and_4 = year_val & 3
    bitwise_and_15 = year_val & 15
    bitwise_and_63 = year_val & 63
    bitwise_and_255 = year_val & 255
    
    div_4 = bitwise_and_4 == 0
    div_100 = (year_val % 100) == 0
    div_400 = (year_val % 400) == 0
    
    is_leap_result = div_4 and (not div_100 or div_400)
    
    return is_leap_result

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 400, 100, 4, 1]
    results = [is_leap(y) for y in test_years]
    print(results)