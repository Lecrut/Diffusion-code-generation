from datetime import datetime

def compute_delta_days(reference: datetime, target: datetime) -> int:
    if reference.tzinfo is not None:
        raise ValueError("Reference datetime must be naive.")
    if target.tzinfo is not None:
        raise ValueError("Target datetime must be naive.")
    interval = target - reference
    return interval.days

if __name__ == '__main__':
    epoch = datetime(2023, 1, 1, 8, 0, 0)
    launch = datetime(2023, 1, 5, 12, 0, 0)
    print(compute_delta_days(epoch, launch))