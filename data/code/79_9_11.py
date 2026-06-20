from datetime import date

def get_next_month_start(input_date: date) -> date:
    month_to_next_month = {
        12: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9,
        9: 10,
        10: 11,
        11: 12
    }
    
    next_month = month_to_next_month[input_date.month]
    next_year = input_date.year if input_date.month != 12 else input_date.year + 1
    
    return date(next_year, next_month, 1)

if __name__ == '__main__':
    sample_date_1 = date(2023, 10, 15)
    result_1 = get_next_month_start(sample_date_1)
    print(f"Input: {sample_date_1}, Output: {result_1}")
    
    sample_date_2 = date(2024, 12, 31)
    result_2 = get_next_month_start(sample_date_2)
    print(f"Input: {sample_date_2}, Output: {result_2}")
    
    sample_date_3 = date(2025, 1, 5)
    result_3 = get_next_month_start(sample_date_3)
    print(f"Input: {sample_date_3}, Output: {result_3}")