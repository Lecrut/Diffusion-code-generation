from datetime import datetime

DAY_OF_WEEK_FORMAT = '%A'

if __name__ == '__main__':
    print(datetime.now().strftime(DAY_OF_WEEK_FORMAT))