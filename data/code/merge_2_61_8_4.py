class TimeConverter:
    def to_components(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return (hours, minutes, secs)
    def format_time(self, seconds, use_24h=True):
        hours, minutes, secs = self.to_components(seconds)
        if not use_24h:
            h_suffix = f" {int(hours)} PM" if int(hours) >= 12 else ""
            m_str = str(int(minutes)).zfill(2) + " " + str(secs).zfill(2)
            return f"{m_str}{h_suffix}"
        return f"{hours:02}:{minutes:02}:{secs:02}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_seconds_list = [3661, 8459, -1]
    for s in test_seconds_list:
        print(f"Input seconds: {s}")
        components = converter.to_components(s)
        formatted_24h = converter.format_time(s, use_24h=True)
        formatted_pm = converter.format_time(s, use_24h=False)
        print(f"Components (int): {components}")
        print(f"Formatted 24h:    {formatted_24h}")
        print(f"Formatted PM/AM:   {formatted_pm}")
        print("---")