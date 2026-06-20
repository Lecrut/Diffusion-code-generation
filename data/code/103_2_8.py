import time

class TimeElapsedCalculator:
    EPOCH = 0
    
    @staticmethod
    def get_elapsed_time():
        current_time = time.time()
        elapsed_seconds = int(current_time - TimeElapsedCalculator.EPOCH)
        hours, remainder = divmod(elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'{hours}h {minutes}m {seconds}s'

if __name__ == '__main__':
    print(TimeElapsedCalculator.get_elapsed_time())