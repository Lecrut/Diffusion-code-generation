class DateUtility:
    @staticmethod
    def convert_date_string(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            return date_obj.strftime('%B %d, %Y')
        except ValueError:
            return "Invalid Date Format"
if __name__ == '__main__':
    import datetime
    date_str1 = "2023-10-27"
    date_str2 = "2024-01-01"
    date_str3 = "2023/10/27"
    date_str4 = "not-a-date"
    print(f"'{date_str1}' converted: {DateUtility.convert_date_string(date_str1)}")
    print(f"'{date_str2}' converted: {DateUtility.convert_date_string(date_str2)}")
    print(f"'{date_str3}' converted: {DateUtility.convert_date_string(date_str3)}")
    print(f"'{date_str4}' converted: {DateUtility.convert_date_string(date_str4)}")