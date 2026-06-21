from datetime import datetime

class TimestampBuckets:
    def __init__(self):
        self.buckets = defaultdict(list)

    def add_timestamp(self, timestamp):
        bucket_key = timestamp.replace(minute=0, second=0, microsecond=0)
        self.buckets[bucket_key].append(timestamp)

    def get_buckets(self):
        return dict(self.buckets)

if __name__ == '__main__':
    timestamps = [
        datetime(2023, 10, 1, 14, 30),
        datetime(2023, 10, 1, 15, 15),
        datetime(2023, 10, 1, 14, 45),
        datetime(2023, 10, 1, 16, 0)
    ]
    
    bucketizer = TimestampBuckets()
    for ts in timestamps:
        bucketizer.add_timestamp(ts)

    print(bucketizer.get_buckets())