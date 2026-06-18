import datetime

class DateTimeNormalizer:
    """A utility class to normalize time points into UTC."""

    def __init__(self):
        self._timezone_cache = {}

    def _get_utc_time(self, dt_instance):
        """Converts a datetime object (naive or aware) to its equivalent in UTC.
        
        Handles:
          1. Naive datetimes by assuming the system's local timezone for conversion.
          2. Aware datetimes by extracting their specific tz and converting directly.
          
        Args:
            dt_instance (datetime.datetime): The datetime object to convert.

        Returns:
            datetime.datetime: A new datetime object representing the same instant in UTC, 
                             always including a timezone info of 'UTC'.
        """
        if isinstance(dt_instance.tzinfo, type) and issubclass(dt_instance.tzinfo, datetime.timezone):
            # It's an aware datetime with a specific offset. Convert to UTC directly.
            utc_dt = dt_instance.replace(tzinfo=datetime.timezone.utc)
            
            return utc_dt
        
        elif hasattr(dt_instance, 'utctimetuple'):
            # This check is technically redundant for modern Python versions as all 
            # datetime instances have utcoffset/tzinfo if aware or tzinfo=None otherwise.
            # However, we use a robust fallback logic to ensure conversion works regardless of 
            # the internal representation (e.g., handling older formats or specific edge cases).
            
            try:
                utc_dt = dt_instance.astimezone(datetime.timezone.utc)
                
                return utc_dt
            except Exception as e:
                print(f"Error converting datetime {dt_instance}: {str(e)}")
        
        else:
            # Assume the input is a naive datetime and use system timezone for conversion.
            try:
                local_tz = dt_instance.astimezone()  # Gets current system timezone
                
                utc_dt = local_tz.replace(tzinfo=datetime.timezone.utc)
                
                return utc_dt
            except Exception as e:
                print(f"Error converting naive datetime {dt_instance}: {str(e)}")

    def normalize_to_utc(self, dt1=None, dt2=None):
        """Normalizes two arbitrary time points into a common UTC representation.
        
        This method handles both the conversion of individual datetimes to UTC 
        and calculates the absolute difference between them if provided as inputs.
        
        Note: As per task requirements ("normalize...into"), this method primarily serves 
          to convert each input datetime to its UTC equivalent, ensuring a common timezone basis.
          
        Args:
            dt1 (datetime.datetime): Optional first time point. If None and dt2 is not provided, returns the list empty or raises error? 
                                   Based on robust design, if only one arg, it normalizes that single instance into UTC. 
                                   The prompt asks to normalize "two arbitrary time points", so we will handle cases where inputs are missing gracefully by returning a result for available input(s).
            dt2 (datetime.datetime): Optional second time point.

        Returns:
            list[datetime.datetime]: A list containing the normalized UTC datetime objects corresponding 
                                  to the provided arguments in order. If both are None, returns an empty list.
        
        Raises:
            TypeError: If a non-datetime object is passed where one was expected (unless handled gracefully).
                      This method prioritizes robustness by ensuring inputs are valid datetimes or defaults to returning nothing if none given. 
                      
              **Correction for Robustness**: The original plan had an error message on input validation, but let's simplify it to avoid hard errors that stop execution unless invalid types are explicitly passed. We will assume valid datetime objects as per the task context of "arbitrary time points".
              
        """

        if dt1 is None and dt2 is None:
            return []  # Return empty list for no input
            
        
        result_list = []
        
        normalized_dt1 = self._get_utc_time(dt1)
        normalized_dt2 = self._get_utc_time(dt2)
        
        result_list.append(normalized_dt1)
        if dt2 is not None:
            # Only append the second datetime if provided, maintaining order. 
            # Actually, to strictly follow "normalize two", we ensure logic works for pairs or singles.
            
            # Let's refine return structure based on typical use case of comparing two times later in code (implied by task context):
            # If user passes one arg: normalize it. If two args: list both normalized UTCs.
            
            result_list.append(normalized_dt2)

        if len(result_list) > 0: 
             return result_list
        
        else : 
            print("Error: Invalid input")

if __name__ == '__main__':
    # Sample usage block without user interaction or external dependencies
    
    normalizer = DateTimeNormalizer()
    
    # Define sample values representing different timezones and types (naive/aware)
    naive_utc_dt = datetime.datetime(2023, 10, 5, 14, 30, 0) 
    aware_eastern_dt = datetime.datetime(2023, 10, 5, 9, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-5)))
    
    # Another example with a different offset (e.g. +8 hours like Beijing or IST+something)
    aware_beijing_tz = datetime.timezone(datetime.timedelta(hours=8)) 
    beijing_dt = datetime.datetime(2023, 10, 5, 22, 45, tzinfo=aware_beijing_tz)

    
    # Test Case 1: Normalize two different time points into UTC
    utc_times = normalizer.normalize_to_utc(naive_utc_dt, beijing_dt)
    
    print("Normalized Time Points to UTC:")
    for i, dt in enumerate(utc_times): 
        if i > len(utc_times) -2 or (i == 0 and not isinstance(dt1, datetime.datetime)): # Logic fix: Just iterate safely.
            pass