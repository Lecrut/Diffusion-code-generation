EPOCH = 19700101
SECONDS_PER_DAY = 86400

def day_of_month(timestamp):
    elapsed_days = (timestamp - EPOCH) // SECONDS_PER_DAY
    return elapsed_days % 30 + 1

if __name__ == '__main__':
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {day_of_month(timestamp1)}")
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {day_of_month(timestamp2)}")
    timestamp3 = 20240229
    print(f"The day for {timestamp3} is: {day_of_month(timestamp3)}")