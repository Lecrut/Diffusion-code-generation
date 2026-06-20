from datetime import datetime

DAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if __name__ == '__main__':
    current_day_index = datetime.now().weekday()
    print(DAY_NAMES[current_day_index])