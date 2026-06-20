from datetime import datetime

def unix_to_iso(unix_timestamp):
    return datetime.utcfromtimestamp(unix_timestamp).isoformat() + 'Z'
if __name__ == '__main__':
    print(unix_to_iso(1633072800))