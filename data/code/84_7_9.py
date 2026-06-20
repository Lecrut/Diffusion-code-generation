def day_of_year(day_number):
    return (day_number - 1) % 365 + 1

if __name__ == '__main__':
    print(day_of_year(365))
    print(day_of_year(366))
    print(day_of_year(1))
    print(day_of_year(2))