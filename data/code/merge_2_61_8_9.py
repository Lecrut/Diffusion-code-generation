class TimeConverter:
    def to_components(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return {"hours": hours, "minutes": minutes, "secs": secs}
    def to_string(self, seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        if h > 0:
            return f"{h}:{m:02d}:{s:02d}"
        elif m > 0:
            return f"0:{m:02d}:{s:02d}"
        else:
            return f"0:00:{s:02d}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_seconds_1 = 3665
    result_dict = converter.to_components(test_seconds_1)
    print(f"Integer Components for {test_seconds_1}:")
    print(result_dict)
    test_string = "7209.5"
    float_val = int(float(test_string))
    formatted_str = converter.to_string(float_val)
    print(f"\nFormatted String for {float_val} seconds:")
    print(formatted_str)