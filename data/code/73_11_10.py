def compute_hourly_delta(epoch_start, epoch_end):
    if type(epoch_start) not in (int, float):
        raise ValueError("start timestamp must be numeric")
    if type(epoch_end) not in (int, float):
        raise ValueError("end timestamp must be numeric")
    raw_delta = epoch_end - epoch_start
    conversion_factor = 3600.0
    result = raw_delta / conversion_factor
    return result

if __name__ == '__main__':
    start_point = 1672531200
    end_point = 1672538400
    output = compute_hourly_delta(start_point, end_point)
    print(output)