from datetime import date
import calendar

TARGET_DAY = 15
REFERENCE_DATE = date(2023, 3, 3)

def find_next_15th(ref_date: date) -> date:
    year = ref_date.year
    month = ref_date.month
    day = ref_date.day
    
    if day <= TARGET_DAY:
        candidate_month = month
        candidate_year = year
    else:
        candidate_month = month + 1
        candidate_year = year
    
    if candidate_month > 12:
        candidate_month = 1
        candidate_year += 1
    
    return date(candidate_year, candidate_month, TARGET_DAY)

if __name__ == '__main__':
    result = find_next_15th(REFERENCE_DATE)
    print(result)