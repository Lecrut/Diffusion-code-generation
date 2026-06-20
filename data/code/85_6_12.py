def days_to_weeks(days):
    return days // 7

if __name__ == '__main__':
    start_date = 20230401
    end_date = 20230501
    print(days_to_weeks(end_date - start_date))