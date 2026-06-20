from datetime import datetime

def time_elapsed_since_midnight():
    midnight = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
    elapsed_seconds = (datetime.now() - midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    print(time_elapsed_since_midnight())