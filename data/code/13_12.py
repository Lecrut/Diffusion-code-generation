import datetime
def scale_time_differences(time_difference_strings):
    result = []
    for ts in time_difference_strings:
        try:
            delta = datetime.timedelta(seconds=int(ts))
            result.append(delta)
        except ValueError:
            pass
    return result
if __name__ == '__main__':
    sample_strings = [
        "60",
        "3600",
        "86400",
        "invalid_time",
        "120000"
    ]
    scaled_deltas = scale_time_differences(sample_strings)
    print(scaled_deltas)