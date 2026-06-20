def months_elapsed(start_month, end_month):
    if not (1 <= start_month <= 12 and 1 <= end_month <= 12):
        raise ValueError("Months must be between 1 and 12")
    return abs(end_month - start_month)

if __name__ == '__main__':
    try:
        result1 = months_elapsed(1, 5)
        print(f"Start: 1, End: 5, Elapsed: {result1}")
        result2 = months_elapsed(10, 3)
        print(f"Start: 10, End: 3, Elapsed: {result2}")
        result3 = months_elapsed(12, 12)
        print(f"Start: 12, End: 12, Elapsed: {result3}")
    except ValueError as e:
        print(e)