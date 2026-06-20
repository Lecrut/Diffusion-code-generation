from datetime import date

def identical_dates_generator(dates):
    for i in range(len(dates) - 1):
        if dates[i] == dates[i + 1]:
            yield True
        else:
            yield False

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 27),
        date(2023, 10, 27),
        date(2023, 11, 27),
        date(2024, 10, 27)
    ]
    
    for result in identical_dates_generator(sample_dates):
        print(result)