from datetime import date

def calculate_year_difference(date1_str: str, date2_str: str) -> int:
    date1 = date.fromisoformat(date1_str)
    date2 = date.fromisoformat(date2_str)
    return abs(date1.year - date2.year)

if __name__ == '__main__':
    result = calculate_year_difference("2020-01-01", "2023-05-15")
    print(result)