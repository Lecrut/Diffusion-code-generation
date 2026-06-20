def classify_day(day):
    if day == 'Saturday' or day == 'Sunday':
        return 'Weekend'
    else:
        return 'Weekday'

if __name__ == '__main__':
    sample_days = ['Monday', 'Friday', 'Saturday', 'Sunday']
    for day in sample_days:
        print(f"{day}: {classify_day(day)}")