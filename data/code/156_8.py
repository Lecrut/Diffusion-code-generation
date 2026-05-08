def find_average(data):
    if not data:
        return 0
    total = 0
    for x in data:
        total += x
    return total / len(data)
if __name__ == '__main__':
    large_list = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
    average = find_average(large_list)
    print(average)