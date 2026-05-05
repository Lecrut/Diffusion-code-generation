import math
def convert_seconds_to_hours(total_seconds):
    hours = total_seconds / 3600.0
    return hours
if __name__ == '__main__':
    sample_duration_1 = 7200
    result_1 = convert_seconds_to_hours(sample_duration_1)
    print(f"Input: {sample_duration_1} seconds, Output: {result_1} hours")
    sample_duration_2 = 3661
    result_2 = convert_seconds_to_hours(sample_duration_2)
    print(f"Input: {sample_duration_2} seconds, Output: {result_2} hours")
    sample_duration_3 = 86400
    result_3 = convert_seconds_to_hours(sample_duration_3)
    print(f"Input: {sample_duration_3} seconds, Output: {result_3} hours")