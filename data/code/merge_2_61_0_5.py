def convert_seconds_to_hm(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}m"
if __name__ == '__main__':
    sample_input = 7265
    result = convert_seconds_to_hm(sample_input)
    print(result)