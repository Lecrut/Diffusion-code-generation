HOURS_TO_MINUTES = 60
HOURS_TO_SECONDS = 3600
MINUTES_TO_SECONDS = 60

class TimeConverter:
    def convert_hours_to_minutes(self, hours):
        return hours * HOURS_TO_MINUTES

    def convert_hours_to_seconds(self, hours):
        return hours * HOURS_TO_SECONDS

    def convert_minutes_to_hours(self, minutes):
        return minutes / HOURS_TO_MINUTES

    def convert_minutes_to_seconds(self, minutes):
        return minutes * MINUTES_TO_SECONDS

    def convert_seconds_to_hours(self, seconds):
        return seconds / HOURS_TO_SECONDS

    def convert_seconds_to_minutes(self, seconds):
        return seconds / MINUTES_TO_SECONDS

if __name__ == '__main__':
    tc = TimeConverter()
    h_val = 2.5
    m_val = 150
    s_val = 7200

    print(tc.convert_hours_to_minutes(h_val))
    print(tc.convert_hours_to_seconds(h_val))
    print(tc.convert_minutes_to_hours(m_val))
    print(tc.convert_minutes_to_seconds(m_val))
    print(tc.convert_seconds_to_hours(s_val))
    print(tc.convert_seconds_to_minutes(s_val))