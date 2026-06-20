from datetime import date

def calculate_month_difference(month1, month2):
    month_to_num = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    return abs(month_to_num[month1] - month_to_num[month2])

if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))