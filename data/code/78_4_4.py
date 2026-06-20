def calculate_shortest_path(month1, month2):
    if month1 > month2:
        return min(month1 - month2, 13 - month1 + month2)
    else:
        return min(month2 - month1, 13 - month2 + month1)
if __name__ == '__main__':
    result = calculate_shortest_path(12, 2)
    print(result)