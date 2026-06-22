def convert_seconds(total_seconds):
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_values = [123456, 789012, 3600, 86400, 0]
    for value in sample_values:
        result = convert_seconds(value)
        print(result)