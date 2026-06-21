TOTAL = 0

def compute_total(data):
    global TOTAL
    for x in data:
        TOTAL += x

def find_average(data):
    if not data:
        return 0
    compute_total(data)
    return TOTAL / len(data)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
    average = find_average(sample_list)
    print(average)