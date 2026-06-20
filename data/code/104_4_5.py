def are_same_date(date1: tuple, date2: tuple) -> bool:
    return date1 == date2

if __name__ == '__main__':
    sample_date1 = (2023, 10, 25)
    sample_date2 = (2023, 10, 25)
    print(are_same_date(sample_date1, sample_date2))