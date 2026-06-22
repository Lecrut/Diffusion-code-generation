from datetime import datetime

TIMESTAMP_LABELS = {
    "epoch_start": 0.0,
    "epoch_mid": 946684800.0,
    "epoch_end": 2524608000.0
}

def is_first_timestamp_before_second(ts1: float, ts2: float) -> bool:
    dt1 = datetime.fromtimestamp(ts1)
    dt2 = datetime.fromtimestamp(ts2)
    return dt1 < dt2

if __name__ == '__main__':
    sample_ts1 = TIMESTAMP_LABELS["epoch_start"]
    sample_ts2 = TIMESTAMP_LABELS["epoch_mid"]
    result = is_first_timestamp_before_second(sample_ts1, sample_ts2)
    print(result)