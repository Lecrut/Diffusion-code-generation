from datetime import datetime

def calculate_net_time_difference(time_differences, delimiter=';'):
    times = [datetime.strptime(t.strip(), "%H:%M:%S") for t in time_differences.split(delimiter)]
    earliest_time = min(times)
    latest_time = max(times)
    net_difference = (latest_time - earliest_time).total_seconds()
    return f"{int(net_difference // 3600)}:{int((net_difference % 3600) // 60)}:{int(net_difference % 60)}"

if __name__ == '__main__':
    sample_input = "12:34:56;09:10:11;15:20:30"
    print(calculate_net_time_difference(sample_input))