import math

MONTH_NAMES = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def month_to_index(month_name):
    return MONTH_NAMES.get(month_name)

def shortest_path_distance(month1, month2):
    distance = abs(month1 - month2)
    circular_distance = 12 - distance
    return min(distance, circular_distance)

if __name__ == '__main__':
    print(shortest_path_distance(12, 2))