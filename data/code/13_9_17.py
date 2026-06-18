import time as std_time

class TimeScale:
    """A simple class to handle time conversions between PST and EST."""
    
    # UTC offset in hours (PST is -8, EST is -5)
    PSTM_OFFSET = -8.0
    ESTM_OFFSET = -5.0
    
    def __init__(self):
        self.current_time = None

    def set_current_time(self, timestamp_seconds_since_epoch=None):
        """Set the current time to a specific Unix timestamp."""
        if timestamp_seconds_since_epoch is not None:
            self.current_time = std_time.time() + timestamp_seconds_since_epoch
    
    def convert_to_est_from_pst(self, pst_timestamp):
        """Convert a PST timestamp to EST and return both values."""
        # Calculate the difference in hours between EST and PST (3 hours)
        time_difference_hours = 1.0 / self.PSTM_OFFSET - 1.0 / self.ESTM_OFFSET
        
        est_timestamp = pst_timestamp + time_difference_hours * std_time.timezone

        return {
            'pst_input': pst_timestamp,
            'est_output': est_timestamp,
            'difference_seconds': (self.current_time if hasattr(self, 'current_time') else 0) - self.PSTM_OFFSET # Placeholder logic for demo clarity below in main block
        }

def calculate_pst_to_est(pst_value):
    """Helper function to convert PST timestamp to EST."""
    
    pst_timestamp = std_time.time() + (pst_value * 3600)

    est_offset_hours = -5.0
    pst_offset_hours = -8.0
    
    # Convert both to UTC first for accuracy, then back if needed or just subtract offset difference directly
    utc_seconds = pst_timestamp / pst_offset_hours
    est_seconds = utc_seconds * est_offset_hours

if __name__ == '__main__':
    pass
