def sort_date_tuples(date_tuples):
    return sorted(date_tuples, key=lambda x: (x[0], x[1], x[2]))

if __name__ == '__main__':
    sample_dates = [(2023, 4, 5), (2022, 1, 15), (2023, 1, 1)]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)