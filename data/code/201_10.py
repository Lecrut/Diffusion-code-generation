import random
if __name__ == '__main__':
    numbers = [10, 25, 32, 48, 15]
    total = sum(numbers)
    count = len(numbers)
    if count > 0:
        mean = total / count
        print(mean)
    else:
        print("The list of numbers is empty.")