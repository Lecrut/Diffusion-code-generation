def convert_duration(total_seconds):
    if total_seconds < 0:
        raise ValueError("total_seconds must be non-negative")
    days = total_seconds // 86400
    remaining_after_days = total_seconds % 86400
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return (days, hours, minutes, seconds)

if __name__ == '__main__':
    sample_value = 99999
    result = convert_duration(sample_value)
    print(result)
    sample_value_2 = 0
    result_2 = convert_duration(sample_value_2)
    print(result_2)
    sample_value_3 = 86401
    result_3 = convert_duration(sample_value_3)
    print(result_3)