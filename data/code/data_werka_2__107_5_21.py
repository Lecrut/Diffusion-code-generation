from datetime import datetime, timedelta, timezone

def format_naive_datetime_with_offset(dt: datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive')
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    dt_utc = dt.replace(tzinfo=timezone.utc)
    delta = dt_utc - epoch
    total_seconds = int(delta.total_seconds())
    sign = '-' if total_seconds < 0 else '+'
    abs_seconds = abs(total_seconds)
    hours = abs_seconds // 3600
    minutes = (abs_seconds % 3600) // 60
    return f'{sign}{hours:02d}{minutes:02d}'

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 15, 14, 30, 0)
    result = format_naive_datetime_with_offset(sample_dt)
    print(result)
    sample_dt_negative = datetime(2023, 10, 15, 14, 30, 0)
    result_negative = format_naive_datetime_with_offset(sample_dt_negative)
    print(result_negative)
    sample_dt_utc = datetime(2023, 10, 15, 14, 30, 0)
    result_utc = format_naive_datetime_with_offset(sample_dt_utc)
    print(result_utc)
    sample_dt_negative_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_negative_offset = format_naive_datetime_with_offset(sample_dt_negative_offset)
    print(result_negative_offset)
    sample_dt_large_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_large_offset = format_naive_datetime_with_offset(sample_dt_large_offset)
    print(result_large_offset)
    sample_dt_small_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_small_offset = format_naive_datetime_with_offset(sample_dt_small_offset)
    print(result_small_offset)
    sample_dt_zero_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_zero_offset = format_naive_datetime_with_offset(sample_dt_zero_offset)
    print(result_zero_offset)
    sample_dt_negative_large_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_negative_large_offset = format_naive_datetime_with_offset(sample_dt_negative_large_offset)
    print(result_negative_large_offset)
    sample_dt_positive_large_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_positive_large_offset = format_naive_datetime_with_offset(sample_dt_positive_large_offset)
    print(result_positive_large_offset)
    sample_dt_mixed_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_mixed_offset = format_naive_datetime_with_offset(sample_dt_mixed_offset)
    print(result_mixed_offset)
    sample_dt_boundary_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_boundary_offset = format_naive_datetime_with_offset(sample_dt_boundary_offset)
    print(result_boundary_offset)
    sample_dt_negative_boundary_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_negative_boundary_offset = format_naive_datetime_with_offset(sample_dt_negative_boundary_offset)
    print(result_negative_boundary_offset)
    sample_dt_positive_boundary_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_positive_boundary_offset = format_naive_datetime_with_offset(sample_dt_positive_boundary_offset)
    print(result_positive_boundary_offset)
    sample_dt_negative_positive_offset = datetime(2023, 10, 15, 14, 30, 0)
    result_negative_positive_offset = format_naive_datetime_with_offset(sample_dt_negative_positive_offset)
    print(result_negative_positive_offset)
    sample_dt_positive_negative_offset = datetime(2023, 10, 15, 14, 30, 0)
    result