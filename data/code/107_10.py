import datetime
if __name__ == '__main__':
    date_string = "2023-10-27"
    try:
        date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        formatted_date = date_object.strftime('%m/%d/%Y')
        print(formatted_date)
    except ValueError:
        print("Invalid date format provided.")