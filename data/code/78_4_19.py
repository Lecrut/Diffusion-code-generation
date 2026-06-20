NUM_MONTHS = 12

def shortest_path_distance(month1, month2):
    return min(abs(month1 - month2), NUM_MONTHS - abs(month1 - month2))

if __name__ == '__main__':
    print(shortest_path_distance(12, 2))