from datetime import datetime

class TimeElapsed:
    START_OF_DAY = datetime(2023, 4, 1, 9, 0, 0)

    @staticmethod
    def get_elapsed_time():
        end_time = datetime.now()
        elapsed_time = end_time - TimeElapsed.START_OF_DAY
        return f"{elapsed_time.seconds // 3600:02}:{(elapsed_time.seconds % 3600) // 60:02}:{elapsed_time.seconds % 60:02}"

if __name__ == '__main__':
    print(TimeElapsed.get_elapsed_time())