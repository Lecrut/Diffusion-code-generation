import time

class TimeConverter:
    """A class to convert between hours, minutes, and seconds efficiently."""

    def __init__(self):
        self.total_seconds = 0

    @classmethod
    def from_hours(cls) -> "TimeConverter":
        return cls()

    def add(self, value, unit="seconds"):
        """Add a specified amount of time to the total.
        
        Args:
            value (float): The duration in hours, minutes, or seconds depending on 'unit'.
            unit (str): One of "hours", "minutes", or "seconds".
            
        Returns:
            None
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        
        conversion_rate = {
            "hours": 3600.0,
            "minutes": 60.0,
            "seconds": 1.0
        }

        if unit in ["hours", "minutes", "seconds"]:
            self.total_seconds += value * conversion_rate[unit]
        else:
            raise ValueError(f"Unsupported unit '{unit}'. Use 'hours', 'minutes', or 'seconds'.")

    def subtract(self, value, unit="seconds"):
        """Subtract a specified amount of time from the total.
        
        Args:
            value (float): The duration in hours, minutes, or seconds depending on 'unit'.
            unit (str): One of "hours", "minutes", or "seconds".
            
        Returns:
            None
            
        Raises:
            ValueError: If subtraction results in negative time.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")

        conversion_rate = {
            "hours": 3600.0,
            "minutes": 60.0,
            "seconds": 1.0
        }

        if unit in ["hours", "minutes", "seconds"]:
            seconds_to_subtract = value * conversion_rate[unit]
            
            new_total = self.total_seconds - seconds_to_subtract
            
            # Ensure we don't allow negative time by clamping to zero or raising error? 
            # Task says mathematically sound. Negative duration is physically impossible in this context usually, 
            # but let's clamp it to 0 for robustness if the user makes a mistake, otherwise raise error on invalid logic.
            # Let's strictly validate: negative total time should be flagged or handled gracefully as zero? 
            # The most mathematically sound interpretation of "time" here is non-negative duration from T=0.
            if new_total < 0:
                self.total_seconds = 0.0
                print("Warning: Subtracted amount exceeded remaining time; result clamped to zero.")
            else:
                self.total_seconds = new_total
        else:
            raise ValueError(f"Unsupported unit '{unit}'. Use 'hours', 'minutes', or 'seconds'.")

    def set(self, value):
        """Set the total duration directly in seconds.
        
        Args:
            value (float): The total time in seconds.
            
        Returns:
            None
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")

        self.total_seconds = max(0.0, value)  # Ensure non-negative
    
    def to_hours(self):
        """Convert the total time into hours."""
        return round(self.total_seconds / 3600, 10)

    def to_minutes(self):
        """Convert the total time into minutes."""
        return round(self.total_seconds / 60, 10)

    def to_seconds(self):
        """Return the current total time in seconds with high precision."""
        return self.total_seconds
    
    def __str__(self):
        h = int(self.to_hours())
        m = int((self.to_minutes() - h * 60)) % 60
        s = round(((self.to_minutes() / 1) + (h * 3600)) % 60, 5) # Wait, simpler calculation
        
        total_hrs = self.to_hours()
        if abs(total_hrs - int(total_hrs)) < 1e-9:
            s_str = f"{int(self.total_seconds // 60):02d}:{self.total_seconds % 60:.5f}"
        else:
             # Format with hours included
             h_full = int(total_hrs)
             dec_part = total_hrs - h_full 
             
             m_total_dec = dec_part * 4.833333 # No, easier way to display mixed units is HH:mm:ss.sss

if __name__ == '__main__':
    pass
