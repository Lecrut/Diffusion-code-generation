class DateTimeFormatter:
    FORMAT_SPEC = "%d/%m/%Y %I:%M %p"

    @staticmethod
    def get_locale_format(dt_obj):
        import locale
        original_locale = locale.getlocale(locale.LC_TIME)
        try:
            locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
            formatted = dt_obj.strftime(DateTimeFormatter.FORMAT_SPEC)
        except locale.Error:
            locale.setlocale(locale.LC_TIME, 'C')
            formatted = dt_obj.strftime(DateTimeFormatter.FORMAT_SPEC)
        finally:
            locale.setlocale(locale.LC_TIME, original_locale)
        return formatted

if __name__ == '__main__':
    import datetime
    sample_dt = datetime.datetime(2023, 10, 5, 14, 30, 0)
    result = DateTimeFormatter.get_locale_format(sample_dt)
    print(result)