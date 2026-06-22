from datetime import datetime

def to_iso_8601():
    now = datetime.now()
    return now.isoformat()

if __name__ == '__main__':
    print(to_iso_8601())