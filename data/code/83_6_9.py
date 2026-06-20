def date_pairs_generator(dates):
    for i in range(len(dates) - 1):
        if dates[i] == dates[i + 1]:
            yield True

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2023-04-01', '2023-04-02', '2023-04-02', '2023-04-03']
    for result in date_pairs_generator(sample_dates):
        print(result)