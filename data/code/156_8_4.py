def find_average_optimized(data):
    if not data:
        return 0
    total = 0
    for x in data:
        total += x
    return total / len(data)
if __name__ == '__main__':
    large_list = list(range(1000000))
    average = find_average_optimized(large_list)
    print(average)