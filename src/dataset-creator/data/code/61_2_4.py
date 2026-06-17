class TimeConverter:
    def convert_seconds_to_hms(self, seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(seconds // 3600)
        remaining_minutes = (seconds % 3600) // 60
        return f"{hours}h {remaining_minutes}m"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        86400,                                  
        3725,                                  
        120,                             
        99999.9                                                                                  
    ]
    print("Conversion Results:")
    for sec in test_cases:
        result = converter.convert_seconds_to_hms(sec)
        print(f"{sec} seconds -> {result}")