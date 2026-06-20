def shortest_path_distance(month1, month2):
    if month1 > 12 or month2 > 12:
        raise ValueError("Month numbers must be between 1 and 12.")
    return min(abs(month1 - month2), 12 - abs(month1 - month2))

if __name__ == '__main__':
    sample_month1 = 8
    sample_month2 = 3
    result = shortest_path_distance(sample_month1, sample_month2)
    print(result)