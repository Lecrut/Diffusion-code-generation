def calculate_list_sum(data):
    total = 0
    for element in data:
        total = total + element
    return total
if __name__ == '__main__':
    numbers = [1, 5, 10, 2, 8]
    result = calculate_list_sum(numbers)
    print(result)