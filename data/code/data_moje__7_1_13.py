class TimeConverter:
    @staticmethod
    def hours_to_minutes(hours):
        if not isinstance(hours, (int, float)) or hours < 0:
            raise ValueError("Hours must be a non-negative number")
        return hours * 60

    @staticmethod
    def hours_to_seconds(hours):
        if not isinstance(hours, (int, float)) or hours < 0:
            raise ValueError("Hours must be a non-negative number")
        return hours * 3600

    @staticmethod
    def minutes_to_hours(minutes):
        if not isinstance(minutes, (int, float)) or minutes < 0:
            raise ValueError("Minutes must be a non-negative number")
        return minutes / 60

    @staticmethod
    def minutes_to_seconds(minutes):
        if not isinstance(minutes, (int, float)) or minutes < 0:
            raise ValueError("Minutes must be a non-negative number")
        return minutes * 60

    @staticmethod
    def seconds_to_hours(seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Seconds must be a non-negative number")
        return seconds / 3600

    @staticmethod
    def seconds_to_minutes(seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Seconds must be a non-negative number")
        return seconds / 60

if __name__ == '__main__':
    converter = TimeConverter()
    hours_value = 2.5
    minutes_value = 45
    seconds_value = 9000

    h_to_m = converter.hours_to_minutes(hours_value)
    h_to_s = converter.hours_to_seconds(hours_value)
    m_to_h = converter.minutes_to_hours(minutes_value)
    m_to_s = converter.minutes_to_seconds(minutes_value)
    s_to_h = converter.seconds_to_hours(seconds_value)
    s_to_m = converter.seconds_to_minutes(seconds_value)

    print(h_to_m)
    print(h_to_s)
    print(m_to_h)
    print(m_to_s)
    print(s_to_h)
    print(s_to_m)