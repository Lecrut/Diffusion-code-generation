from datetime import date

def calculate_month_difference(month1, month2):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    month1_index = months.index(month1)
    month2_index = months.index(month2)
    return abs(month1_index - month2_index)

if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))