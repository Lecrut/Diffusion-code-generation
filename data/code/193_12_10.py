def aggregate_numbers(data):
    return sum(data)

if __name__ == '__main__':
    sample_list = [10, 25, 30, 5]
    total = aggregate_numbers(sample_list)
    print(total)