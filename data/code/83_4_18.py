from datetime import date

def dates_are_identical(date_str1: str, date_str2: str) -> bool:
    return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)
if __name__ == '__main__':
    sample_dates = {'same': ('2023-05-01', '2023-05-01'), 'different': ('2023-05-01', '2023-05-02')}
    print(dates_are_identical(*sample_dates['same']))
    print(dates_are_identical(*sample_dates['different']))