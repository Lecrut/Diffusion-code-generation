from datetime import date
def identical_date_pairs_generator(dates):
    n = len(dates)
    for i in range(n):
        for j in range(n):
            if dates[i] == dates[j]:
                yield True
if __name__ == '__main__':
    sample_dates = [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 1), date(2023, 3, 1)]
    generator = identical_date_pairs_generator(sample_dates)
    results = list(generator)
    print(results)