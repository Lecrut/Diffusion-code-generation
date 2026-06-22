def convert_to_appropriate_unit(total_seconds):
    if total_seconds >= 3600:
        return total_seconds / 3600, "hours"
    elif total_seconds >= 60:
        return total_seconds / 60, "minutes"
    else:
        return total_seconds, "seconds"

if __name__ == '__main__':
    sample_values = [3661, 90, 45, 7200, 60]
    for val in sample_values:
        result, unit = convert_to_appropriate_unit(val)
        print(f"{val} seconds = {result} {unit}")