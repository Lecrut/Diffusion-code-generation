from datetime import datetime

def sort_datetimes(data):
    timestamp_tuples = []
    for dt in data:
        ts = dt.timestamp()
        timestamp_tuples.append((ts, dt))
    timestamp_tuples.sort(key=lambda pair: pair[0])
    result = []
    for _, dt in timestamp_tuples:
        result.append(dt)
    return result

if __name__ == '__main__':
    entry_one = datetime(2024, 2, 15, 9, 0)
    entry_two = datetime(2023, 12, 31, 23, 59, 59)
    entry_three = datetime(2024, 2, 15, 9, 0)
    entry_four = datetime(2023, 1, 1, 0, 0)
    input_list = [entry_one, entry_two, entry_three, entry_four]
    output_list = sort_datetimes(input_list)
    print(output_list)