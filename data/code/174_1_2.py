def calculate_average(scores):
    if not scores:
        return 0
    total = sum(scores.values())
    count = len(scores)
    return total / count
if __name__ == '__main__':
    data1 = {"Alice": 85, "Bob": 92, "Charlie": 78}
    data2 = {}
    data3 = {"X": 100}
    print(calculate_average(data1))
    print(calculate_average(data2))
    print(calculate_average(data3))