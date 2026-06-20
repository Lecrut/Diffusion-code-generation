if __name__ == '__main__':
    sample_dates = [(2023, 1, 15), (2022, 12, 25), (2024, 1, 1)]
    sorted_dates = sorted(sample_dates)
    print("Sorted Dates:")
    for date in sorted_dates:
        print(f"Year: {date[0]}, Month: {date[1]}, Day: {date[2]}")