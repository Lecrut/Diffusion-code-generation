import time

class TimeElapsedCalculator:
    def __init__(self, reference_point=None):
        if reference_point is not None:
            self.reference = reference_point
        else:
            self.reference = time.time()
    
    def calculate(self):
        current_time = time.time()
        if self.reference is None:
            raise ValueError("Reference point not set")
        
        total_seconds = current_time - self.reference
        if total_seconds < 0:
            raise ValueError("Elapsed time cannot be negative")
        
        hours = int(total_seconds // 3600)
        remainder = total_seconds % 3600
        minutes = int(remainder // 60)
        seconds = remainder % 60
        
        return {
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }

def compute_elapsed_time_since_midnight():
    now = time.time()
    seconds_in_day = 86400
    midnight_timestamp = now - (now % seconds_in_day)
    
    elapsed = TimeElapsedCalculator(midnight_timestamp)
    return elapsed.calculate()

if __name__ == '__main__':
    result = compute_elapsed_time_since_midnight()
    print(result)