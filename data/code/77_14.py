import sys
def convert_time_to_minutes(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_minutes = hours * 60 + minutes + seconds
    return total_minutes
if __name__ == '__main__':
    time_input = '1:30:00'
    result = convert_time_to_minutes(time_input)
    print(result)