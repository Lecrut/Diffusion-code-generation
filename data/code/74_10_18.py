from datetime import datetime

def get_current_day():
    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    try:
        current_day_index = datetime.now().weekday()
        if not (0 <= current_day_index < 7):
            raise ValueError("Invalid day index")
        return days_of_week[current_day_index]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    print(get_current_day())