import datetime
def scale_time_differences(time_diff_strings):
    result = []
    for t_str in time_diff_strings:
        try:
            delta = datetime.timedelta(seconds=int(t_str))
            result.append(delta)
        except ValueError:
            pass
    return result
if __name__ == '__main__':
    sample_data = [
        "60",
        "120",
        "invalid_time",
        "3600",
        "90000"
    ]
    scaled_deltas = scale_time_differences(sample_data)
    print(scaled_deltas)