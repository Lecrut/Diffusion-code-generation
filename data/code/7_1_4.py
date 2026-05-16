class TimeConverter:
    def __init__(self):
        pass
    def to_seconds(self, hours, minutes, seconds):
        return (hours * 3600) + (minutes * 60) + seconds
    def from_seconds(self, total_seconds):
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return hours, minutes, seconds
    def to_hms(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds
if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours = 2
    sample_minutes = 30
    sample_seconds = 15
    total_seconds = converter.to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(f"Input: {sample_hours}h, {sample_minutes}m, {sample_seconds}s")
    print(f"Total seconds: {total_seconds}")
    h, m, s = converter.from_seconds(total_seconds)
    print(f"Converted back: {h}h, {m}m, {s}s")
    another_total_seconds = 7385
    h2, m2, s2 = converter.to_hms(another_total_seconds)
    print(f"Total seconds: {another_total_seconds}")
    print(f"Converted to HMS: {h2}h, {m2}m, {s2}s")