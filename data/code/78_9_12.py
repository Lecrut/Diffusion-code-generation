def calculate_month_difference(month1, month2):
    return abs(month2 - month1)

if __name__ == '__main__':
    start_month = 5
    end_month = 10
    difference = calculate_month_difference(start_month, end_month)
    print(difference)