def day_of_year(days_passed):
    return days_passed % 365 + 1
if __name__ == '__main__':
    print(day_of_year(400))
    print(day_of_year(730))