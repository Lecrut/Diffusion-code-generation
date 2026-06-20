from datetime import date

def compare_dates(date_str1, date_str2):
    return min(date.fromisoformat(date_str1), date.fromisoformat(date_str2))

if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-03-15'))