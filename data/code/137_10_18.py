def classify_day(day):
    if day == 'Saturday' or day == 'Sunday':
        return 'Weekend'
    else:
        return 'Weekday'

if __name__ == '__main__':
    sample_day_1 = 'Wednesday'
    sample_day_2 = 'Sunday'
    
    result_1 = classify_day(sample_day_1)
    result_2 = classify_day(sample_day_2)
    
    print(f"Day: {sample_day_1}, Classification: {result_1}")
    print(f"Day: {sample_day_2}, Classification: {result_2}")