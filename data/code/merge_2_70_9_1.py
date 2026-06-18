def compare_distance_values(value1: float, value2: float) -> int:
    return int(value1 - value2)
if __name__ == '__main__':
    distance_a = 10**20 + 5000.0                                                                    
    distance_b = 10**20 - 3000.0                                         
    result = compare_distance_values(distance_a, distance_b)
    if result > 0:
        print("Distance A is greater than Distance B.")
    elif result < 0:
        print("Distance A is less than Distance B.")
    else:
        print("Distances are equal.")