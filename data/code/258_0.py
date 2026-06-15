if __name__ == '__main__':
    data = [(1, 5), (2, 8), (3, 10), (4, 12)]
    sum_first = 0
    sum_second = 0
    count = len(data)
    for first, second in data:
        sum_first += first
        sum_second += second
    average_first = sum_first / count
    average_second = sum_second / count
    print(f"Average of first elements: {average_first}")
    print(f"Average of second elements: {average_second}")