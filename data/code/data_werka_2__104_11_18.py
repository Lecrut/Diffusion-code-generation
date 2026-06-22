from datetime import datetime

def days_between(reference: datetime, target: datetime) -> int:
    if reference.tzinfo is not None:
        raise ValueError("Reference must be naive")
    if target.tzinfo is not None:
        raise ValueError("Target must be naive")
    return (target - reference).days

if __name__ == '__main__':
    dt_a = datetime(2024, 2, 1, 12, 0, 0)
    dt_b = datetime(2024, 2, 10, 12, 0, 0)
    print(days_between(dt_a, dt_b))