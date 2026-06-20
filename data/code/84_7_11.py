def day_of_year(epoch_days, total_days):
    return (epoch_days + total_days) % 365

if __name__ == '__main__':
    epoch = 0
    days_passed = 182
    print(day_of_year(epoch, days_passed))