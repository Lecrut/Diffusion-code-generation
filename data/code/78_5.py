def shortest_month_distance(month1, month2):
    diff = abs(month1 - month2)
    return min(diff, 12 - diff)
if __name__ == '__main__':
    m1 = 12
    m2 = 2
    result = shortest_month_distance(m1, m2)
    print(result)