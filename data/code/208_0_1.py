import random
if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    total = sum(numbers)
    count = len(numbers)
    if count > 0:
        mean = total / count
        print(mean)
    else:
        print("The list of numbers is empty.")