def shortest_path_distance(month1: int, month2: int) -> int:
    return min(abs(month1 - month2), 12 - abs(month1 - month2))

if __name__ == '__main__':
    print(shortest_path_distance(12, 2))