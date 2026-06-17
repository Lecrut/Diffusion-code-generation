from datetime import date
def get_past_dates(input_date: date, n_years: int) -> list[date]:
    return [input_date.replace(year=input_date.year - i * n_years) for i in range(1, 5)]
if __name__ == '__main__':
    sample_date = date(2023, 6, 15)
    result_dates = get_past_dates(sample_date, 1)
    print(result_dates)