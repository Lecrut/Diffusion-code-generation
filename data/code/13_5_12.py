import datetime

class DateTimeNormalizer:
    """A utility class to normalize arbitrary time points into UTC."""

    def __init__(self, source_time_1=None, source_time_2=None):
        self.source_time_1 = None
        self.source_time_2 = None
        
        if isinstance(source_time_1, datetime.datetime) or (isinstance(source_time_1, str)):
            try:
                # Attempt to parse string input as ISO format with timezone info first
                dt_obj = source_time_1.replace(microsecond=int(float(str(source_time_1).split('.')[-1]) * 10**6)) if '.' in str(source_time_1) else datetime.datetime.fromisoformat(source_time_1)
            except Exception:
                # Fallback for other string formats or direct object passing logic below
                try: 
                    self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_1)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
                except: 
                    self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Ensure the object is a datetime instance
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime
            try: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            except: 
                self.source_time_1 = source_time_1.replace(microsecond=int(float(str(self._parse_input_to_dt(source_time_2)).split('.')[-1]) * 10**6)) if isinstance(source_time_1, str) and '.' in str(source_time_1) else None
            
            # Finalize conversion to datetime

if __name__ == '__main__':
    pass
