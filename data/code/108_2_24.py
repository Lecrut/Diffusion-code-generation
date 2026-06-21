import time

def fetch_day_of_month():
    timestamp = time.time()
    local_structured = time.localtime(timestamp)
    if local_structured is None:
        raise ValueError("Failed to retrieve local time")
    return local_structured.tm_mday

if __name__ == '__main__':
    result = fetch_day_of_month()
    print(result)