def shortest_path_distance(month1, month2):
    diff = abs(month1 - month2)
    return min(diff, 12 - diff)

if __name__ == '__main__':
    print(shortest_path_distance(12, 2))