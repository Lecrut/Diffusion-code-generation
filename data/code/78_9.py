import sys
def calculate_month_difference(month1, month2):
    if month2 > month1:
        return month2 - month1
    else:
        return month1 - month2
if __name__ == '__main__':
    month_a = 5
    month_b = 10
    difference = calculate_month_difference(month_a, month_b)
    print(difference)