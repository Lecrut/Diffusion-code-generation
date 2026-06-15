if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30]
    largest = input_data[0]
    for number in input_data:
        if number > largest:
            largest = number
    print(largest)