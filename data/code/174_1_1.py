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
    average1 = calculate_average(data1)
    average2 = calculate_average(data2)
    average3 = calculate_average(data3)
    print(f"Average for data1: {average1}")
    print(f"Average for data2: {average2}")
    print(f"Average for data3: {average3}")