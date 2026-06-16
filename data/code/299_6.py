import datetime
def is_weekend(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    day_of_week = date_obj.weekday()
    return day_of_week >= 5
test_dates = [
    ('2023-10-08', True),            
    ('2023-10-09', True),          
    ('2023-10-07', False),                           
    ('2023-10-10', False)                            
]
results = []
for date_str, expected in test_dates:
    actual = is_weekend(date_str)
    test_result = actual == expected
    results.append((date_str, actual, expected, test_result))
for date_str, actual, expected, passed in results:
    print(f"Date: {date_str}, Actual: {actual}, Expected: {expected}, Passed: {passed}")
if __name__ == '__main__':
    pass