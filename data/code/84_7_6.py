def day_of_year(epoch_days):
    return (epoch_days - 1) % 365 + 1

if __name__ == '__main__':
    sample_epoch_days = 400
    print(day_of_year(sample_epoch_days))