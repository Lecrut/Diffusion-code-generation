import datetime

def convert_pst_to_est(pst_datetime):
    """
    Converts a given PST (Pacific Standard Time) datetime to EST (Eastern Standard Time).
    
    Note: This implementation assumes standard time zones without daylight saving adjustments,
    as DST rules vary by region and year. In production code, use the 'zoneinfo' library or pytz
    for accurate historical and future timezone conversions including DST.
    
    PST is UTC-8 during Standard Time.
    EST is UTC-5 during Standard Time.
    The difference between them in standard time is 3 hours (EST is ahead).
    """
    # Convert to UTC first, then apply the offset for EST
    utc_time = pst_datetime.replace(tzinfo=datetime.timezone.utc) - datetime.timedelta(hours=8)
    
    est_timezone = datetime.timezone(datetime.timedelta(hours=-5))
    est_time = utc_time.astimezone(est_timezone)
    
    return est_time

def calculate_difference(pst_dt, est_dt):
    """Calculates the time difference between two datetimes."""
    delta = est_dt - pst_dt
    hours_diff = int(delta.total_seconds() // 3600)
    minutes_diff = int((delta.total_seconds() % 3600) // 60)
    
    return {
        'total_minutes': int(delta.total_seconds()),
        'hours_difference': hours_diff,
        'minutes_difference': minutes_diff
    }

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # Using a fixed date to avoid DST complications in this simplified example.
    pst_sample = datetime.datetime(2023, 10, 5, 14, 30)
    
    print(f"Input PST Time: {pst_sample}")
    
    est_time = convert_pst_to_est(pst_sample)
    print(f"Converted EST Time: {est_time}")
    
    diff_info = calculate_difference(pst_sample, est_time)
    print(f"\nTime Difference Details:")
    print(f"Total minutes difference: {diff_info['total_minutes']}")
    print(f"Hours difference (EST - PST): {diff_info['hours_difference']:+d} hours")