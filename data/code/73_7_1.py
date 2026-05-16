import datetime
if __name__ == '__main__':
    date1_str = "2023-03-12"
    date2_str = "2023-03-15"
    date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
    difference = date2 - date1
    print(difference)