class TimeCalculator:
    EPOCH = datetime.datetime(1970, 1, 1)
    
    @staticmethod
    def get_current_time_milliseconds():
        return int((datetime.datetime.now() - TimeCalculator.EPOCH).total_seconds() * 1000)

if __name__ == '__main__':
    milliseconds = TimeCalculator.get_current_time_milliseconds()
    print(milliseconds)