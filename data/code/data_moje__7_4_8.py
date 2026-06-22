from datetime import datetime, timedelta

class TimeConverter:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400
    SECONDS_PER_WEEK = 604800
    SECONDS_PER_MONTH = 2629746
    SECONDS_PER_YEAR = 31556952

    def __init__(self):
        self.units = {'seconds': 1, 'minutes': self.SECONDS_PER_MINUTE, 'hours': self.SECONDS_PER_HOUR, 'days': self.SECONDS_PER_DAY, 'weeks': self.SECONDS_PER_WEEK, 'months': self.SECONDS_PER_MONTH, 'years': self.SECONDS_PER_YEAR}

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self.units:
            raise ValueError(f'Unsupported unit: {from_unit}')
        if to_unit not in self.units:
            raise ValueError(f'Unsupported unit: {to_unit}')
        value_in_seconds = value * self.units[from_unit]
        result = value_in_seconds / self.units[to_unit]
        return result

    def convert_to_seconds(self, value, unit):
        unit = unit.lower()
        if unit not in self.units:
            raise ValueError(f'Unsupported unit: {unit}')
        return value * self.units[unit]

    def convert_from_seconds(self, seconds, unit):
        unit = unit.lower()
        if unit not in self.units:
            raise ValueError(f'Unsupported unit: {unit}')
        return seconds / self.units[unit]

    def get_all_conversions(self, value, from_unit):
        from_unit = from_unit.lower()
        if from_unit not in self.units:
            raise ValueError(f'Unsupported unit: {from_unit}')
        result = {}
        for target_unit in self.units:
            if target_unit != from_unit:
                result[target_unit] = self.convert(value, from_unit, target_unit)
        return result

    def parse_duration_string(self, duration_str):
        total_seconds = 0
        current_num = ''
        for char in duration_str:
            if char.isdigit() or char == '.':
                current_num += char
            elif char.lower() in 'ydwms':
                if current_num:
                    num = float(current_num)
                    if char.lower() == 'y':
                        total_seconds += num * self.SECONDS_PER_YEAR
                    elif char.lower() == 'd':
                        total_seconds += num * self.SECONDS_PER_DAY
                    elif char.lower() == 'w':
                        total_seconds += num * self.SECONDS_PER_WEEK
                    elif char.lower() == 'm':
                        total_seconds += num * self.SECONDS_PER_MONTH
                    elif char.lower() == 's':
                        total_seconds += num * self.SECONDS_PER_MINUTE
                    current_num = ''
            else:
                raise ValueError(f'Invalid character in duration: {char}')
        return total_seconds

    def format_duration(self, seconds):
        years = int(seconds // self.SECONDS_PER_YEAR)
        remainder = seconds % self.SECONDS_PER_YEAR
        months = int(remainder // self.SECONDS_PER_MONTH)
        remainder = remainder % self.SECONDS_PER_MONTH
        days = int(remainder // self.SECONDS_PER_DAY)
        remainder = remainder % self.SECONDS_PER_DAY
        hours = int(remainder // self.SECONDS_PER_HOUR)
        remainder = remainder % self.SECONDS_PER_HOUR
        minutes = int(remainder // self.SECONDS_PER_MINUTE)
        seconds_left = int(remainder % self.SECONDS_PER_MINUTE)
        parts = []
        if years > 0:
            parts.append(f'{years} years')
        if months > 0:
            parts.append(f'{months} months')
        if days > 0:
            parts.append(f'{days} days')
        if hours > 0:
            parts.append(f'{hours} hours')
        if minutes > 0:
            parts.append(f'{minutes} minutes')
        if seconds_left > 0 or not parts:
            parts.append(f'{seconds_left} seconds')
        return ', '.join(parts)
if __name__ == '__main__':
    converter = TimeConverter()
    print('=== Basic Conversions ===')
    print('1 year to days:', converter.convert(1, 'years', 'days'))
    print('24 hours to days:', converter.convert(24, 'hours', 'days'))
    print('365 days to years:', converter.convert(365, 'days', 'years'))
    print('1 hour to minutes:', converter.convert(1, 'hours', 'minutes'))
    print('90 minutes to hours:', converter.convert(90, 'minutes', 'hours'))
    print('1 day to seconds:', converter.convert(1, 'days', 'seconds'))
    print('31536000 seconds to years:', converter.convert(31536000, 'seconds', 'years'))
    print('\n=== All Conversions from 1 Day ===')
    all_conv = converter.get_all_conversions(1, 'days')
    for unit, val in all_conv.items():
        print(f'  1 day = {val:.4f} {unit}')
    print('\n=== Parse Duration String ===')
    parsed_secs = converter.parse_duration_string('1d12h30m15s')
    print("Parsed '1d12h30m15s' to seconds:", parsed_secs)
    print('Back to hours:', converter.convert(parsed_secs, 'seconds', 'hours'))
    print('\n=== Format Duration ===')
    total_seconds = 366.2425 * 24 * 3600
    print(f'{total_seconds} seconds formatted:', converter.format_duration(total_seconds))
    half_year_seconds = converter.convert(0.5, 'years', 'seconds')
    print(f'Half year in seconds:', half_year_seconds)
    print('Half year formatted:', converter.format_duration(half_year_seconds))
    print('\n=== Month Conversions ===')
    print('1 month to days:', converter.convert(1, 'months', 'days'))
    print('30 days to months:', converter.convert(30, 'days', 'months'))
    print('12 months to years:', converter.convert(12, 'months', 'years'))
    print('\n=== Week Conversions ===')
    print('1 week to days:', converter.convert(1, 'weeks', 'days'))
    print('52 weeks to years:', converter.convert(52, 'weeks', 'years'))