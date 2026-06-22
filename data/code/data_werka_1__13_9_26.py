from dateutil import parser

def parse_time_difference(time_str):
    return parser.parse(time_str).replace(tzinfo=None) - parser.parse('00:00').replace(tzinfo=None)

def total_elapsed_time(time_differences):
    total_seconds = sum((parse_time_difference(td).total_seconds() for td in time_differences))
    return int(total_seconds / 60)
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '2 hours']
    total_minutes = total_elapsed_time(sample_times)
    print(total_minutes)