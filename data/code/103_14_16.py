from datetime import datetime

def get_elapsed_time():
    start_time = datetime(2023, 4, 1, 9, 0, 0)
    end_time = datetime.now()
    elapsed = end_time - start_time
    return str(elapsed).split('.')[0]

if __name__ == '__main__':
    print(get_elapsed_time())