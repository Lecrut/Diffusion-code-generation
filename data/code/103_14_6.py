from datetime import datetime

def get_elapsed_time():
    start_time = datetime(2023, 4, 1, 12, 0, 0)
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    return str(elapsed_time).split('.')[0]

if __name__ == '__main__':
    print(get_elapsed_time())