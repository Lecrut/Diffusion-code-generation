import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class DateComparator:
    def compare(self, date1_str, date2_str):
        if not (validate_date(date1_str) and validate_date(date2_str)):
            raise ValueError("Both dates must be in 'YYYY-MM-DD' format.")
        
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
        
        if date1 < date2:
            return (date1, date2)
        else:
            return (date2, date1)

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.compare("2023-10-26", "2023-10-25")
    print(f"Comparing 2023-10-26 and 2023-10-25: {result1}")
    
    result2 = comparator.compare("2024-01-01", "2023-12-31")
    print(f"Comparing 2024-01-01 and 2023-12-31: {result2}")
    
    result3 = comparator.compare("1999-01-01", "2000-01-01")
    print(f"Comparing 1999-01-01 and 2000-01-01: {result3}")