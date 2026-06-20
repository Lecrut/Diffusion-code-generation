def day_of_year(days_passed):
    if days_passed < 0:
        raise ValueError("Days passed must be non-negative")
    return (days_passed % 365) + 1

if __name__ == '__main__':
    print(day_of_year(0))
    print(day_of_year(364))
    print(day_of_year(365))