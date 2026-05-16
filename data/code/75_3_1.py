from datetime import datetime
def date_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    return date2 - date1
if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-10"
    difference = date_difference(date1, date2)
    print(difference)