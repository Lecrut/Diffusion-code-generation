def compute_average(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    sample_list = list(range(1, 1000001))
    average = compute_average(sample_list)
    print(average)