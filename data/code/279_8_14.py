def square_numbers(number_list):
    squared = []
    for number in number_list:
        squared.append(number ** 2)
    return squared

if __name__ == '__main__':
    sample_values = [3, 4, 5, 6, 7]
    result = square_numbers(sample_values)
    print(result)