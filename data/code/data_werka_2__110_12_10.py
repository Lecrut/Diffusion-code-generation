def sort_dates_chronologically(date_collection):
    def to_comparable_tuple(date_tuple):
        year, month, day = date_tuple
        return (year, month, day)

    def extract_sort_key(date_tuple):
        return to_comparable_tuple(date_tuple)

    sorted_collection = sorted(date_collection, key=extract_sort_key)
    return sorted_collection

if __name__ == '__main__':
    raw_dates = [
        (2000, 2, 29),
        (1995, 11, 12),
        (2000, 1, 1),
        (1995, 11, 1),
        (2000, 2, 28)
    ]
    result = sort_dates_chronologically(raw_dates)
    print(result)