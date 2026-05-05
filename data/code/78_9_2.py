import sys
def calculate_month_difference(month1_str, month2_str):
    month1 = int(month1_str)
    month2 = int(month2_str)
    return abs(month1 - month2)
if __name__ == '__main__':
    month1 = "5"
    month2 = "10"
    difference = calculate_month_difference(month1, month2)
    print(difference)