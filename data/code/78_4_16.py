def shortest_path_distance(month1, month2):
    diff = abs(month1 - month2)
    return min(diff, 12 - diff)

if __name__ == '__main__':
    sample_month1 = 10
    sample_month2 = 3
    print(shortest_path_distance(sample_month1, sample_month2))