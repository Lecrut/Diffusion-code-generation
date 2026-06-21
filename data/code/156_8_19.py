MEAN_CALCULATION_THRESHOLD = 10**5

def calculate_mean(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    if count > MEAN_CALCULATION_THRESHOLD:
        return total / count
    else:
        running_sum = 0
        for number in data:
            running_sum += number
        return running_sum / count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = calculate_mean(sample_list)
    print(result)