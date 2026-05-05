def calculate_time_difference(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    if len(lines) < 2:
        return None, None
    try:
        time1 = float(lines[0].strip())
        time2 = float(lines[1].strip())
        if time2 > time1:
            difference = time2 - time1
            return time1, time2, difference
        else:
            difference = time1 - time2
            return time2, time1, difference
    except ValueError:
        return None, None, None
if __name__ == '__main__':
    sample_file_path = "time_data.txt"
    with open(sample_file_path, 'w') as f:
        f.write("10:30:00\n")
        f.write("14:45:00\n")
    start_time, end_time, elapsed_time = calculate_time_difference(sample_file_path)
    if elapsed_time is not None:
        print(f"Start time: {start_time}")
        print(f"End time: {end_time}")
        print(f"Total elapsed time: {elapsed_time}")
    else:
        print("Error reading time data or file format is incorrect.")