import datetime
def check_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
        weekday = date_obj.weekday()
        if weekday >= 5:
            return True
        else:
            return False
    except ValueError:
        return None
if __name__ == '__main__':
    dates_to_check = [
        '01/01/2024',                    
        '01/06/2024',                    
        '03/15/2024',                    
        '12/25/2023',                    
        '02/17/2024',                       
        '02/18/2024',                      
        '02/19/2024',                    
        '02/20/2024',                      
        '35/10/2024',                                               
    ]
    for date_str in dates_to_check:
        result = check_weekend(date_str)
        print(f"Date: {date_str}, Is Weekend: {result}")