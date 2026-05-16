import sys
def calculate_month_difference(month1_str, month2_str):
    month1 = int(month1_str)
    month2 = int(month2_str)
    return abs(month1 - month2)
if __name__ == '__main__':
    month_a = "5"
    month_b = "10"
    difference = calculate_month_difference(month_a, month_b)
    print(difference)