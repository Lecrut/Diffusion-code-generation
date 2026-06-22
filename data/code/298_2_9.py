from datetime import datetime

def time_difference(time1, time2):
    format = "%H:%M:%S"
    tdelta = datetime.strptime(time2, format) - datetime.strptime(time1, format)
    return tdelta.seconds // 3600, (tdelta.seconds % 3600) // 60, tdelta.seconds % 60

if __name__ == '__main__':
    result = time_difference("14:30:00", "17:45:30")
    print(result)