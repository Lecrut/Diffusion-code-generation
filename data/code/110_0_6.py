def sort_chronological_dates(input_dates):
    if not input_dates:
        return []
    date_tuples = []
    for current_date_str in input_dates:
        year_part = current_date_str[0:4]
        month_part = current_date_str[5:7]
        day_part = current_date_str[8:10]
        year_int = int(year_part)
        month_int = int(month_part)
        day_int = int(day_part)
        date_tuples.append((year_int, month_int, day_int, current_date_str))
    sorted_tuples = sorted(date_tuples, key=lambda t: (t[0], t[1], t[2]))
    return [t[3] for t in sorted_tuples]

if __name__ == '__main__':
    raw_dates = ['1999-12-31', '2000-01-01', '1999-12-30', '2000-02-29', '1999-01-01']
    ordered_dates = sort_chronological_dates(raw_dates)
    print(ordered_dates)