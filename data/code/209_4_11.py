from functools import reduce

def sum_and_count(data):
    return (reduce(lambda acc, x: (acc[0] + x, acc[1] + 1), data, (0, 0)))

def calculate_average(data):
    total, count = sum_and_count(data)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    data = [2, 4, 6, 8, 10]
    print(f"Average of {data}: {calculate_average(data)}")