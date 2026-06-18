import datetime
from concurrent.futures import ThreadPoolExecutor
def subtract_years(timestamps: list, years_to_subtract: int) -> list:
    results = []
    def process_date(ts):
        try:
            dt = datetime.datetime.fromisoformat(ts).replace(tzinfo=datetime.timezone.utc)
            new_dt = dt - datetime.timedelta(days=years_to_subtract * 365.2425)
            return new_dt.isoformat()
        except Exception as e:
            results.append(f"Error processing {ts}: {e}")
            raise
    with ThreadPoolExecutor(max_workers=len(timestamps)) as executor:
        futures = [executor.submit(process_date, ts) for ts in timestamps]
        for future in futures:
            try:
                result = future.result()
                if isinstance(result, str):
                    results.append(result)
                else:
                    raise TypeError("Expected string from process_date")
            except Exception as e:
                pass
    return results
if __name__ == '__main__':
    input_timestamps = [
        "2023-12-31T23:59:59",
        "2024-06-15T12:00:00",
        "2025-01-01T00:00:00"
    ]
    years = 5
    output_timestamps = subtract_years(input_timestamps, years)
    print("Original Timestamps:")
    for ts in input_timestamps:
        print(f"{ts}")
    print("\nTimestamps after subtraction:")
    for ts in output_timestamps:
        print(ts)