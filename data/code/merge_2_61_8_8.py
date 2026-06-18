class TimeConverter:
    def to_components(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return {
            "hours": hours,
            "minutes": minutes,
            "seconds": secs
        }
    def to_formatted_string(self, seconds):
        components = self.to_components(seconds)
        h_str = f"{components['hours']:02d}" if components["hours"] > 0 else ""
        m_str = f"{components['minutes']:02d}"
        s_str = f"{components['seconds']:02d}"
        parts = []
        if h_str:
            parts.append(f"{h_str}:{m_str}")
        return f"{parts[0]}:{s_str}" if parts else f"00:{s_str}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_seconds_list = [3661, 89452, -1]
    for sec in test_seconds_list:
        print(f"\nInput Seconds: {sec}")
        components = converter.to_components(sec)
        formatted_str = converter.to_formatted_string(abs(sec)) if sec < 0 else converter.to_formatted_string(sec)
        print("Integer Components:", components)
        print("Formatted String Output:", formatted_str)