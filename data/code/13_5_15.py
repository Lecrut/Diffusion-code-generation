import datetime

class DateTimeNormalizer:
    """A utility class to normalize arbitrary time points into UTC."""

    @staticmethod
    def _to_utc_naive(dt):
        """Convert a timezone-aware or naive datetime to UTC and return as naive."""
        if dt.tzinfo is not None:
            # Convert aware datetime to UTC
            utc_dt = dt.astimezone(datetime.timezone.utc)
            return utc_dt.replace(tzinfo=None)  # Return naive in UTC
        else:
            # Assume input is local time and convert using system timezone, then strip tz
            # Note: Without explicit 'from_utc' or specific offset info for a generic naive datetime,
            # we assume it represents the current effective local time. 
            # To be strictly robust without knowing the source TZ of a naive datetime, 
            # standard practice is to treat naive as UTC if ambiguous, OR raise an error.
            # However, the prompt asks to handle "all necessary timezone conversions".
            # A common convention when converting from 'naive' (assuming it's local) to UTC:
            # We cannot accurately convert without knowing the source TZ. 
            # The most robust interpretation for a generic naive input in this context is that 
            # if no tzinfo exists, we treat it as already being in UTC or assume system timezone.
            # Let's adopt the convention: Naive -> Treat as UTC to avoid assumptions about system locale.
            return dt

    def normalize_to_utc(self, start_point, end_point):
        """
        Normalize two arbitrary time points into a common UTC representation.
        
        Args:
            start_point (datetime.datetime): The starting datetime point. Can be naive or aware.
            end_point (datetime.datetime): The ending datetime point. Can be naive or aware.

        Returns:
            tuple: A tuple containing the normalized start and end datetimes as UTC-naive objects.
        
        Raises:
            TypeError: If inputs are not datetime instances.
        """
        if not isinstance(start_point, datetime.datetime):
            raise TypeError("start_point must be a datetime instance.")
        if not isinstance(end_point, datetime.datetime):
            raise TypeError("end_point must be a datetime instance.")

        # Normalize start point to UTC (naive)
        normalized_start = self._to_utc_naive(start_point)
        
        # Normalize end point to UTC (naive)
        normalized_end = self._to_utc_naive(end_point)

        return normalized_start, normalized_end

if __name__ == '__main__':
    # Hard-coded sample values representing different timezones and naive datetimes
    
    # Sample 1: Aware datetime in US/Eastern (UTC-5 during winter example)
    eastern_aware = datetime.datetime(2023, 6, 15, 14, 30, tzinfo=datetime.timezone(datetime.timedelta(hours=-5)))
    
    # Sample 2: Naive datetime representing London time (assumed local context for naive input handling strategy used)
    # Our implementation treats naive as UTC to ensure robustness without system dependency assumptions.
    london_naive = datetime.datetime(2023, 6, 15, 22, 45)

    normalizer = DateTimeNormalizer()
    
    start_utc, end_utc = normalizer.normalize_to_utc(eastern_aware, london_naive)
    
    print(f"Original Start: {eastern_aware}")
    print(f"Normalized Start (UTC): {start_utc}")
    print("-" * 30)
    print(f"Original End: {london_naive}")
    print(f"Normalized End (UTC): {end_utc}")

    # Additional test case with mixed naive and aware inputs where source TZ is unknown for the naive one.
    # We treat the second naive input as UTC per our robustness strategy defined in _to_utc_naive.
    
    paris_aware = datetime.datetime(2023, 6, 15, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=+2)))
    us_naive = datetime.datetime(2023, 6, 15, 9, 0)

    start_utc_2, end_utc_2 = normalizer.normalize_to_utc(paris_aware, us_naive)
    
    print("-" * 30)
    print(f"\nTest Case 2:")
    print(f"Original Start (Paris): {paris_aware}")
    print(f"Normalized Start (UTC): {start_utc_2}")
    print(f"Original End (US Naive, treated as UTC): {us_naive}")
    print(f"Normalized End (UTC): {end_utc_2}")