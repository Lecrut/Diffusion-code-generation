from datetime import datetime

def iso_8601_format():
    now = datetime.now()
    return now.isoformat()

if __name__ == '__main__':
    print(iso_8601_format())