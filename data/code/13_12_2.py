import datetime
def scale_time_differences(time_strings):
    result = []
    for time_str in time_strings:
        try:
            delta = datetime.timedelta(seconds=int(time_str))
            result.append(delta)
        except ValueError:
            pass
    return result
if __name__ == '__main__':
    sample_times = [
        "60",
        "3600",
        "90061",
        "invalid_time",
        "1200"
    ]
    scaled_deltas = scale_time_differences(sample_times)
    print(scaled_deltas)