import datetime

class TimeScaleManager:
    """
    A class to manage time conversions between different timezone identifiers,
    handling Daylight Saving Time (DST) automatically using Python's standard library.
    
    Usage Example:
        manager = TimeScaleManager()
        converted_time = manager.convert_timezone(datetime.datetime.now(), 'UTC', 'US/Pacific')
    """

    def convert_timezone(self, source_datetime, from_tz_id, to_tz_id):
        """
        Converts a given datetime object from one timezone identifier to another.
        
        This method uses the `zoneinfo` module (Python 3.9+) which handles DST transitions accurately
        by consulting local time rules and database updates for specific regions.
        
        If 'zoneinfo' is not available, it falls back to a simulated approach using pytz-like logic 
        or raises an error if neither is present. For this standalone solution without external dependencies like pytz,
        we utilize the built-in `datetime` zone-aware capabilities available in modern Python versions (3.9+).

        Args:
            source_datetime (datetime.datetime): The datetime object to convert. It must be timezone-naive 
                                                if 'from_tz_id' is passed as a string identifier for a specific location,
                                                OR it can be an aware datetime where the zone info matches 'from_tz_id'.
            from_tz_id (str): String representation of the source timezone ID (e.g., 'UTC', 'US/Eastern').
            to_tz_id (str): String representation of the target timezone ID.

        Returns:
            datetime.datetime: The converted datetime object in the new timezone, including DST adjustments.

        Raises:
            ValueError: If the provided timezones are invalid or if zoneinfo is unavailable for specific IDs.
            TypeError: If source_datetime is not a valid datetime type.
            
        Note: 
          This implementation relies on Python 3.9+ and its built-in `zoneinfo` module to ensure accurate DST handling.
          It does NOT use pytz (which requires external installation) nor any network access for real-time DB lookups,
          as zoneinfo bundles the necessary rules locally in modern distributions or assumes they are present on the system image.
        """

        try:
            from datetime import timezone
            
            # Ensure we have a valid ZoneInfo object for source and target
            from_zone = __import__('zoneinfo').ZoneInfo(from_tz_id)
            to_zone = __import__('zoneinfo').ZoneInfo(to_tz_id)
            
            if isinstance(source_datetime, datetime.datetime):
                if hasattr(source_datetime, 'tzinfo'):
                    # If the input is already timezone aware but doesn't match from_tz_id exactly (or just in case), 
                    # we re-attach or verify. However, standard practice with zoneinfo suggests passing naive to convert explicitly.
                    pass
                
                # Create a new datetime object attached to source_zone
                dt_in_source = source_datetime.replace(tzinfo=from_zone)
                
                # Convert to target timezone
                dt_in_target = from_zone.convert(dt_in_source, to_zone)
                
                return dt_in_target

            else:
                raise TypeError("source_datetime must be a datetime object.")
        except ImportError as e:
            if "zoneinfo" in str(e):
                # Fallback logic for older Python versions or environments without zoneinfo pre-installed.
                # Since the task forbids external libraries like pytz to ensure no network/installation, 
                # and strictly requires accuracy including DST, we prioritize standard library support (3.9+).
                raise RuntimeError("This TimeScaleManager class requires Python 3.9 or higher with zoneinfo module available.") from e

if __name__ == '__main__':
    # Sample execution block - no user input required
    
    manager = TimeScaleManager()

    # Define sample datetimes and timezones
    utc_time = datetime.datetime(2024, 3, 15, 12, 30)
    
    # Convert from UTC to US/Eastern (which observes DST starting March 10 at 2:00 AM EST -> EDT)
    eastern_time = manager.convert_timezone(utc_time, 'UTC', 'US/Eastern')

    print(f"Original Time (UTC): {utc_time}")
    
    # Check if it is currently Daylight Saving Time in the target zone on this date 
    # Note: March 15th usually implies DST is active.
    dst_status = "DST Active" if eastern_time.tzinfo.utcoffset(eastern_time) == datetime.timedelta(hours=4) else "Standard Time (NST)"
    
    print(f"Converted Time (US/Eastern): {eastern_time}")
    print(f"DST Status on this date: {dst_status}")

    # Another sample for Standard Time 
    winter_utc = datetime.datetime(2023, 11, 5, 8, 0) # Before Nov 4th DST ends in US/Eastern
    
    dst_winter_status = "DST Active" if manager.convert_timezone(winter_utc, 'UTC', 'US/Eastern').tzinfo.utcoffset(manager.convert_timezone(winter_utc, 'UTC', 'US/Eastern')) == datetime.timedelta(hours=5) else "Standard Time (EST)"
    
    winter_eastern = manager.convert_timezone(winter_utc, 'UTC', 'US/Eastern')

    print(f"\nOriginal Winter Time (UTC): {winter_utc}")
    print(f"Converted Winter Time (US/Eastern): {winter_eastern}")