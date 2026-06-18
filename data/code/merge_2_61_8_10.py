class SecondsConverter:
    def to_components(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        minutes = int(seconds // 60)
        remaining_seconds_after_minutes = abs(int((seconds - minutes * 60))) % 1
        hours = minutes // 3600 if isinstance(minutes, (int, float)) else 0
        actual_hours = int(hours)
        final_remaining = seconds - (actual_hours * 3600 + remaining_seconds_after_minutes)
        return {
            'hours': actual_hours,
            'minutes': minutes % 60 if isinstance(minutes, int) else abs(int(minutes)) % 60,
            'seconds': round(final_remaining, 2)
        }
    def to_formatted_string(self, seconds):
        try:
            components = self.to_components(seconds)
            return f"{components['hours']:0>2}:{components['minutes']:0>2}:{components['seconds']:.2f}"
        except Exception as e:
            raise ValueError(f"Conversion failed due to error: {e}")
if __name__ == '__main__':
    converter = SecondsConverter()
    sample_seconds_integers = [3665, 8401.75, -90]
    for s in sample_seconds_integers:
        print(f"Input seconds: {s}")
        components_result = converter.to_components(s)
        print("Components:", components_result)
        formatted_result = converter.to_formatted_string(s)
        print("Formatted string:", formatted_result)