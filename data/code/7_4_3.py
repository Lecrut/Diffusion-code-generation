class TimeConverter:
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400
    SECONDS_IN_MONTH = 2629746
    SECONDS_IN_YEAR = 31556952

    def __init__(self):
        self.units = {
            'year': self.SECONDS_IN_YEAR,
            'month': self.SECONDS_IN_MONTH,
            'day': self.SECONDS_IN_DAY,
            'hour': self.SECONDS_IN_HOUR,
            'minute': self.SECONDS_IN_MINUTE,
            'second': 1
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in self.units:
            raise ValueError(f"Invalid from_unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Invalid to_unit: {to_unit}")

        if from_unit == to_unit:
            return value

        seconds = value * self.units[from_unit]
        result = seconds / self.units[to_unit]
        return result

    def convert_to_dict(self, value, from_unit):
        from_unit = from_unit.lower()
        if from_unit not in self.units:
            raise ValueError(f"Invalid from_unit: {from_unit}")

        total_seconds = value * self.units[from_unit]
        result = {}
        for unit, factor in self.units.items():
            result[unit] = total_seconds / factor
        return result

    def convert_from_dict(self, time_dict):
        total_seconds = 0
        for unit, value in time_dict.items():
            unit = unit.lower()
            if unit not in self.units:
                raise ValueError(f"Invalid unit: {unit}")
            total_seconds += value * self.units[unit]
        return total_seconds

    def format_time(self, seconds):
        years = int(seconds // self.SECONDS_IN_YEAR)
        remaining = seconds % self.SECONDS_IN_YEAR
        months = int(remaining // self.SECONDS_IN_MONTH)
        remaining %= self.SECONDS_IN_MONTH
        days = int(remaining // self.SECONDS_IN_DAY)
        remaining %= self.SECONDS_IN_DAY
        hours = int(remaining // self.SECONDS_IN_HOUR)
        remaining %= self.SECONDS_IN_HOUR
        minutes = int(remaining // self.SECONDS_IN_MINUTE)
        seconds = int(remaining % self.SECONDS_IN_MINUTE)

        parts = []
        if years:
            parts.append(f"{years} year(s)")
        if months:
            parts.append(f"{months} month(s)")
        if days:
            parts.append(f"{days} day(s)")
        if hours:
            parts.append(f"{hours} hour(s)")
        if minutes:
            parts.append(f"{minutes} minute(s)")
        if seconds:
            parts.append(f"{seconds} second(s)")

        if not parts:
            return "0 seconds"

        if len(parts) == 1:
            return parts[0]

        if len(parts) == 2:
            return f"{parts[0]} and {parts[1]}"

        last_part = parts.pop()
        return ", ".join(parts) + f", and {last_part}"

def convert_time(value, from_unit, to_unit):
    converter = TimeConverter()
    return converter.convert(value, from_unit, to_unit)

def convert_time_to_all_units(value, from_unit):
    converter = TimeConverter()
    return converter.convert_to_dict(value, from_unit)

def calculate_total_seconds(time_dict):
    converter = TimeConverter()
    return converter.convert_from_dict(time_dict)

def format_duration(seconds):
    converter = TimeConverter()
    return converter.format_time(seconds)

if __name__ == '__main__':
    converter = TimeConverter()

    print("=== Direct Conversions ===")
    print(f"1 year to days: {converter.convert(1, 'year', 'day')}")
    print(f"30 days to months: {converter.convert(30, 'day', 'month')}")
    print(f"1 hour to seconds: {converter.convert(1, 'hour', 'second')}")
    print(f"7200 seconds to hours: {converter.convert(7200, 'second', 'hour')}")
    print(f"0.5 months to days: {converter.convert(0.5, 'month', 'day')}")

    print("\n=== Conversion to All Units ===")
    result = converter.convert_to_dict(1, 'year')
    print(f"1 year in all units: {result}")

    result = converter.convert_to_dict(24, 'hour')
    print(f"24 hours in all units: {result}")

    print("\n=== Calculate Total Seconds ===")
    time_dict = {'year': 1, 'month': 3, 'day': 15, 'hour': 6, 'minute': 30, 'second': 45}
    total_seconds = converter.convert_from_dict(time_dict)
    print(f"Total seconds for {time_dict}: {total_seconds}")

    print("\n=== Format Duration ===")
    print(f"3661 seconds: {converter.format_time(3661)}")
    print(f"31556952 seconds (1 year): {converter.format_time(31556952)}")
    print(f"0 seconds: {converter.format_time(0)}")
    print(f"60 seconds: {converter.format_time(60)}")
    print(f"3600 seconds: {converter.format_time(3600)}")

    print("\n=== Using Standalone Functions ===")
    print(f"Convert 2 hours to minutes: {convert_time(2, 'hour', 'minute')}")
    print(f"All units for 1 day: {convert_time_to_all_units(1, 'day')}")
    print(f"Total seconds: {calculate_total_seconds({'hour': 1, 'minute': 30})}")
    print(f"Formatted 90 seconds: {format_duration(90)}")