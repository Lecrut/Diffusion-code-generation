if __name__ == '__main__':
    pairs = [
        (10, 20),
        (5, 15),
        (8, 2),
        (12, 30)
    ]
    sum_firsts = 0
    sum_seconds = 0
    count = len(pairs)
    for first, second in pairs:
        sum_firsts += first
        sum_seconds += second
    average_firsts = sum_firsts / count
    average_seconds = sum_seconds / count
    print(f"Average of the first numbers: {average_firsts}")
    print(f"Average of the second numbers: {average_seconds}")