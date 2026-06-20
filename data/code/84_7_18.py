def day_of_year(days_passed):
    return (days_passed + 1) % 365

if __name__ == '__main__':
    sample_days = 123
    print(day_of_year(sample_days))