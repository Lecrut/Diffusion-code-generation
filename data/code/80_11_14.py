import datetime

class DateComparator:
    @staticmethod
    def compare(date1_str: str, date2_str: str) -> tuple:
        try:
            date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
            date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
            if date1 < date2:
                return (date1, date2)
            else:
                return (date2, date1)
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    result1 = comparator.compare(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    
    date_c = "2024-01-01"
    date_d = "2023-12-31"
    result2 = comparator.compare(date_c, date_d)
    print(f"Comparing {date_c} and {date_d}: {result2}")
    
    try:
        date_e = "2025-05-10"
        date_f = "2025/05/10"
        result3 = comparator.compare(date_e, date_f)
    except ValueError as e:
        print(e)