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
    sample_inputs = [
        "60",
        "3600",
        "86400",
        "invalid_time",
        "120000"
    ]
    scaled_deltas = scale_time_differences(sample_inputs)
    print(scaled_deltas)