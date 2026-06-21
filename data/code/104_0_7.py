from datetime import datetime

def check_earlier(first: datetime, second: datetime) -> bool:
    first_epoch = first.replace(tzinfo=None).timestamp()
    second_epoch = second.replace(tzinfo=None).timestamp()
    return first_epoch < second_epoch

if __name__ == '__main__':
    start = datetime(2025, 3, 10, 14, 20, 0)
    end = datetime(2025, 3, 10, 15, 20, 0)
    result = check_earlier(start, end)
    print(result)