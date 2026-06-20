def validate_month(month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")

def shortest_path_distance(month1, month2):
    validate_month(month1)
    validate_month(month2)
    return min(abs(month1 - month2), 12 - abs(month1 - month2))

if __name__ == '__main__':
    print(shortest_path_distance(12, 2))