import datetime

class WeightEntry:
    """Represents a single weight recording."""
    
    def __init__(self, date_str=None):
        self.date = None
        
        if date_str is not None:
            try:
                # Handle ISO format or default to current time string if empty/invalid but provided context implies we can parse dates
                parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                self.date = parsed_date
            except ValueError:
                pass
        
        # If no valid date was set in init (and not None), default to today's time for new entries if needed later, 
        # but here we strictly store what is passed. For consistency in stats calculation without external input prompts,
        # if self.date remains None and a Date object isn't expected yet, we'll handle it gracefully.

    def add_days(self, days):
        """Adds specific number of days to the date."""
        if not isinstance(self.date, datetime.datetime) or self.date is None:
            return
        
        new_date = self.date + datetime.timedelta(days=days)
        
        try:
            self.date = datetime.datetime.strftime(new_date, "%Y-%m-%d %H:%M")
        except Exception: 
            # Fallback to just appending string representation logic if strftime fails (unlikely for valid datetime objects created here)
            pass
            
    def add_months(self, months):
        """Adds specific number of months to the date."""
        if not isinstance(self.date, datetime.datetime) or self.date is None:
            return

if __name__ == '__main__':
    pass
