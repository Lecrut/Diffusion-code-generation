import math
def convert_duration_to_minutes(duration_str):
    parts = duration_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_minutes = hours * 60 + minutes + seconds / 60
    return total_minutes
if __name__ == '__main__':
    duration1 = '1:30:00'
    result1 = convert_duration_to_minutes(duration1)
    print(result1)
    duration2 = '0:05:45'
    result2 = convert_duration_to_minutes(duration2)
    print(result2)
    duration3 = '2:15:00'
    result3 = convert_duration_to_minutes(duration3)
    print(result3)