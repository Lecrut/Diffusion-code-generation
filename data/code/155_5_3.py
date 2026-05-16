def calculate_list_sum(data):
    total = 0
    for element in data:
        total = total + element
    return total
if __name__ == '__main__':
    my_list = [1, 5, 10, 2, 8]
    result = calculate_list_sum(my_list)
    print(result)