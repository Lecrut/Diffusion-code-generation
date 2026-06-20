from datetime import datetime

def date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs(date1 - date2)

if __name__ == '__main__':
    date1 = "2023-02-15"
    date2 = "2023-01-20"
    difference = date_difference(date1, date2)
    print(difference)