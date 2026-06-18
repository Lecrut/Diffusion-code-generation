def time_to_seconds(days: int) -> int:
    if not isinstance(days, (int, float)):
        raise TypeError(f"Expected an integer or float for days, got {type(days).__name__}")
    SECONDS_PER_DAY = 24 * 60 * 60
    return int(days) * SECONDS_PER_DAY
if __name__ == '__main__':
    test_cases = [1, 365, 8760]
    print("Time to Seconds Conversion Results:")
    print("-" * 40)
    for day_count in test_cases:
        seconds_result = time_to_seconds(day_count)
        formatted_output = f"{day_count} days -> {seconds_result:,} seconds"
        print(formatted_output)
    massive_days = 10**9 + 7                                                              
    result_massive = time_to_seconds(massive_days)
    print("-" * 40)
    print(f"{massive_days} days -> {result_massive:,} seconds")