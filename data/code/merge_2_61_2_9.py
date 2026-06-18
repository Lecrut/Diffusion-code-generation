class TimeFormatter:
    def convert_seconds_to_hms(self, seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Input must be a non-negative numeric value.")
        hours = int(seconds // 3600)
        remaining_minutes = (seconds % 3600) // 60
        minutes = int(remaining_minutes)
        secs_displayed = seconds - (hours * 3600 + minutes * 60)
        return f"{hours:02d}:{minutes:02d}"
if __name__ == '__main__':
    formatter = TimeFormatter()
    test_cases = [
        1,                                          
        3599,                                    
        7200,                          
        86400,                             
    ]
    for sec in test_cases:
        result = formatter.convert_seconds_to_hms(sec)
        print(f"{sec} seconds -> {result}")