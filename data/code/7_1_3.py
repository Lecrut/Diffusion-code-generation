class TimeConverter:
    def __init__(self):
        pass
    def to_total_seconds(self, hours, minutes, seconds):
        return (hours * 3600) + (minutes * 60) + seconds
    def from_total_seconds(self, total_seconds):
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return hours, minutes, seconds
    def convert_to_hms(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds
if __name__ == '__main__':
    converter = TimeConverter()
    sample_h = 2
    sample_m = 30
    sample_s = 15
    total_seconds = converter.to_total_seconds(sample_h, sample_m, sample_s)
    print(f"Input: {sample_h}h, {sample_m}m, {sample_s}s")
    print(f"Total seconds: {total_seconds}")
    h, m, s = converter.from_total_seconds(total_seconds)
    print(f"Converted back: {h}h, {m}m, {s}s")
    h_out, m_out, s_out = converter.convert_to_hms(total_seconds)
    print(f"Converted to HMS: {h_out}h, {m_out}m, {s_out}s")
    another_test = 86399
    h_test, m_test, s_test = converter.convert_to_hms(another_test)
    print(f"Test case (86399s): {h_test}h, {m_test}m, {s_test}s")