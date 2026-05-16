from datetime import datetime
import locale
def format_date_localized(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        try:
            locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_TIME, 'English_United States.1252')
            except locale.Error:
                pass
        formatted_date = date_obj.strftime('%d-%b-%Y')
        return formatted_date
    except ValueError:
        return "Invalid date format"
if __name__ == '__main__':
    date_input = '2023-10-27'
    result = format_date_localized(date_input)
    print(result)