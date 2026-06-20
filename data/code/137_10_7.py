def classify_day(day):
    if day == 'Saturday' or day == 'Sunday':
        return 'Weekend'
    else:
        return 'Weekday'
if __name__ == '__main__':
    sample_day1 = 'Sunday'
    sample_day2 = 'Tuesday'
    print(classify_day(sample_day1))
    print(classify_day(sample_day2))