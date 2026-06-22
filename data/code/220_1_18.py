def calculate_average(lst):
    total = 0
    count = 0
    for num in lst:
        total += num
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_list = [7, 8, 9]
    average = calculate_average(sample_list)
    print(average)