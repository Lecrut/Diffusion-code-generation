import random
if __name__ == '__main__':
    random_numbers = [1, 2, 3, 4, 5]
    squared_numbers = []
    for number in random_numbers:
        squared_numbers.append(number * number)
    print(squared_numbers)