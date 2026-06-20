def calculate_day_of_year(days_passed):
    return (days_passed % 365) + 1

if __name__ == '__main__':
    sample_days = 420
    print(calculate_day_of_year(sample_days))