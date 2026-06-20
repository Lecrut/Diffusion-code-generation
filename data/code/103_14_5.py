from datetime import datetime

def get_elapsed_time():
    start = datetime(2023, 4, 1, 9, 0, 0)
    end = datetime.now()
    elapsed = end - start
    return str(elapsed).split('.')[0]

if __name__ == '__main__':
    print(get_elapsed_time())