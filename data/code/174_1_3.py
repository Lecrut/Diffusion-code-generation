def calculate_average(scores):
    if not scores:
        return 0
    total = sum(scores.values())
    count = len(scores)
    return total / count
if __name__ == '__main__':
    data1 = {"Math": 90, "Science": 85, "History": 78}
    data2 = {}
    data3 = {"A": 10, "B": 20, "C": 30}
    avg1 = calculate_average(data1)
    avg2 = calculate_average(data2)
    avg3 = calculate_average(data3)
    print(f"Average for data1: {avg1}")
    print(f"Average for data2: {avg2}")
    print(f"Average for data3: {avg3}")