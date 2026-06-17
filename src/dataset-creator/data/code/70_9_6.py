def compare_distances(distance_a: float, distance_b: float) -> str:
    if not isinstance(distance_a, (int, float)) or not isinstance(distance_b, (int, float)):
        raise TypeError("Both inputs must be numeric values.")
    distance_diff = abs(distance_a - distance_b)
    if distance_a > distance_b:
        return "Distance A is greater than Distance B"
    elif distance_b > distance_a:
        return "Distance B is greater than Distance A"
    else:
        return "Distances are equal"
if __name__ == '__main__':
    d1 = 9223372036854775807                                                      
    d2 = -9223372036854775808                                                     
    result_a_b = compare_distances(d1, d2)
    print(result_a_b)