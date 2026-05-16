def calculate_day_of_year(days_since_epoch, epoch_start_day):
    day_of_year = (days_since_epoch - epoch_start_day) % 365
    if day_of_year < 0:
        day_of_year += 365
    return day_of_year
if __name__ == '__main__':
    days_since_epoch_1 = 100
    epoch_start_day_1 = 1
    result_1 = calculate_day_of_year(days_since_epoch_1, epoch_start_day_1)
    print(f"Days since epoch: {days_since_epoch_1}, Epoch start day: {epoch_start_day_1}, Day of year: {result_1}")
    days_since_epoch_2 = 366
    epoch_start_day_2 = 1
    result_2 = calculate_day_of_year(days_since_epoch_2, epoch_start_day_2)
    print(f"Days since epoch: {days_since_epoch_2}, Epoch start day: {epoch_start_day_2}, Day of year: {result_2}")
    days_since_epoch_3 = 1
    epoch_start_day_3 = 1
    result_3 = calculate_day_of_year(days_since_epoch_3, epoch_start_day_3)
    print(f"Days since epoch: {days_since_epoch_3}, Epoch start day: {epoch_start_day_3}, Day of year: {result_3}")
    days_since_epoch_4 = 365
    epoch_start_day_4 = 1
    result_4 = calculate_day_of_year(days_since_epoch_4, epoch_start_day_4)
    print(f"Days since epoch: {days_since_epoch_4}, Epoch start day: {epoch_start_day_4}, Day of year: {result_4}")