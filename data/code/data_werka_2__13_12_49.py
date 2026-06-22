def aggregate_time_differences(time_diffs):
    total_seconds = 0
    for diff in time_diffs:
        parts = diff.split()
        if len(parts) != 2 and len(parts) != 4:
            raise ValueError(f"Invalid time difference format: {diff}")
        
        value1, unit1 = parts[0], parts[1]
        try:
            value1 = int(value1)
        except ValueError:
            raise ValueError(f"Invalid numeric value in time difference: {value1}")

        if len(parts) == 4:
            value2, unit2 = parts[2], parts[3]
            try:
                value2 = int(value2)
            except ValueError:
                raise ValueError(f"Invalid numeric value in time difference: {value2}")
        else:
            value2, unit2 = 0, ''

        if unit1 == 'hours':
            total_seconds += value1 * 3600
        elif unit1 == 'minutes':
            total_seconds += value1 * 60
        else:
            raise ValueError(f"Unsupported unit in time difference: {unit1}")

        if len(parts) == 4:
            if unit2 == 'hours':
                total_seconds += value2 * 3600
            elif unit2 == 'minutes':
                total_seconds += value2 * 60
            else:
                raise ValueError(f"Unsupported unit in time difference: {unit2}")

    return total_seconds

if __name__ == '__main__':
    sample_time_diffs = [
        "2 hours and 30 minutes",
        "1 hour 45 minutes",
        "30 minutes",
        "2 hours"
    ]
    print(aggregate_time_differences(sample_time_diffs))