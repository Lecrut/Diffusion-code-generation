def find_average(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    large_list = list(range(1000000))
    average = find_average(large_list)
    print(average)