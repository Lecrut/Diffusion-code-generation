from datetime import datetime

def iso_8601_format():
    now = datetime.now()
    return now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')

if __name__ == '__main__':
    print(iso_8601_format())