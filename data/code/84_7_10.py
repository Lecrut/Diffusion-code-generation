def day_of_year(days_passed):
    base_day = 1
    year_length = 365
    return (days_passed + base_day) % year_length
if __name__ == '__main__':
    print(day_of_year(0))
    print(day_of_year(364))
    print(day_of_year(729))