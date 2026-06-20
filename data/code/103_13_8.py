import time

def calculate_fractional_day():
    current_time = time.time()
    start_of_day = int(current_time) // (24 * 3600) * (24 * 3600)
    elapsed_seconds_today = current_time - start_of_day
    total_seconds_in_a_day = 24 * 3600
    fractional_part = elapsed_seconds_today / total_seconds_in_a_day
    return fractional_part

if __name__ == '__main__':
    sample_fractional_day = calculate_fractional_day()
    print(f"Fraction of day that has passed: {sample_fractional_day:.4f}")