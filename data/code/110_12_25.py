DATE_COMPARISON_KEYS = (0, 1, 2)

def sort_date_tuples(date_list):
    return sorted(date_list, key=lambda date: tuple(date[key] for key in DATE_COMPARISON_KEYS))

if __name__ == '__main__':
    sample_dates = [(2023, 4, 5), (2022, 1, 1), (2023, 1, 15)]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)