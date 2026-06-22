from datetime import date

def year_difference(date_str1: str, date_str2: str) -> int:
    year1 = int(date_str1[:4])
    month1 = int(date_str1[5:7])
    day1 = int(date_str1[8:10])
    year2 = int(date_str2[:4])
    month2 = int(date_str2[5:7])
    day2 = int(date_str2[8:10])
    
    d1 = date(year1, month1, day1)
    d2 = date(year2, month2, day2)
    
    diff_years = d2.year - d1.year
    
    if (d2.month, d2.day) < (d1.month, d1.day):
        diff_years -= 1
        
    return abs(diff_years)

if __name__ == '__main__':
    result = year_difference("2020-02-29", "2021-02-28")
    print(result)