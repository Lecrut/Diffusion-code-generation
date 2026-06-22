from datetime import date

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    date1 = date.fromisoformat(date1_str)
    date2 = date.fromisoformat(date2_str)
    years = date2.year - date1.year
    if (date2.month, date2.day) < (date1.month, date1.day):
        years -= 1
    return abs(years)

if __name__ == '__main__':
    result = compute_year_difference("2020-02-29", "2023-02-28")
    print(result)