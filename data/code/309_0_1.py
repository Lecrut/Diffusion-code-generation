def calculate_list_sum(data):
    total = 0
    for element in data:
        total += element
    return total
if __name__ == '__main__':
    sample_list = [1, 5, 10, -3, 8]
    result = calculate_list_sum(sample_list)
    print(result)