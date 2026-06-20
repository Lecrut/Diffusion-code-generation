import time

def calculate_fraction_of_day():
    current_time = time.time()
    start_of_day = time.mktime((current_time // 86400) * 86400)
    elapsed_seconds = current_time - start_of_day
    total_seconds_in_day = 86400
    fraction_of_day = elapsed_seconds / total_seconds_in_day
    return fraction_of_day

if __name__ == '__main__':
    sample_fraction = calculate_fraction_of_day()
    print(sample_fraction)