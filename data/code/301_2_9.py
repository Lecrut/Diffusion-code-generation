from datetime import datetime

def to_iso_8601():
    return datetime.now().isoformat()

if __name__ == '__main__':
    print(to_iso_8601())