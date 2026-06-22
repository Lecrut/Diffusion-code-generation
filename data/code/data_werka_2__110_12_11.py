def sort_date_tuples(dates):
    if not dates:
        return []
    sorted_dates = []
    for date in dates:
        year, month, day = date
        inserted = False
        for i, existing in enumerate(sorted_dates):
            ex_year, ex_month, ex_day = existing
            if year < ex_year:
                sorted_dates.insert(i, date)
                inserted = True
                break
            if year == ex_year:
                if month < ex_month:
                    sorted_dates.insert(i, date)
                    inserted = True
                    break
                if month == ex_month:
                    if day < ex_day:
                        sorted_dates.insert(i, date)
                        inserted = True
                        break
        if not inserted:
            sorted_dates.append(date)
    return sorted_dates

if __name__ == '__main__':
    sample_dates = [
        (2023, 5, 10),
        (2020, 12, 25),
        (2023, 5, 1),
        (2020, 1, 1),
        (2021, 11, 30)
    ]
    result = sort_date_tuples(sample_dates)
    print(result)