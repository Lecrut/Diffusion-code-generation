import datetime

class DateDecorator:
    DAY_NAMES = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]

    @staticmethod
    def prepend_day_name(date_obj):
        return f"{DateDecorator.DAY_NAMES[date_obj.weekday()]} {date_obj}"

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            date_obj = func(*args, **kwargs)
            return self.prepend_day_name(date_obj)
        return wrapper

if __name__ == '__main__':
    decorator = DateDecorator()
    
    @decorator
    def get_current_date():
        return datetime.datetime.now().date()

    print(get_current_date())