NUMBERS_DICT = {1: [10, 20, 30], 2: [40, 50, 60]}

def get_average(data):
    if not data:
        return 0
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = NUMBERS_DICT[1]
    average = get_average(sample_data)
    print(average)