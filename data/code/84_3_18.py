import datetime

class DateParser:
    @staticmethod
    def day_of_year(date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return date_obj.timetuple().tm_yday
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

if __name__ == '__main__':
    parser = DateParser()
    print(parser.day_of_year('2023-10-27'))