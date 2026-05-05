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
    sample_file_content = "10:00:00\n14:30:00"
    with open("time_data.txt", "w") as f:
        f.write(sample_file_content)
    t1, t2, diff = calculate_time_difference("time_data.txt")
    if diff is not None:
        print(f"Time point 1: {t1}")
        print(f"Time point 2: {t2}")
        print(f"Total elapsed time: {diff}")