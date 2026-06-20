def check_negatives():
    numbers = [-10, 5, -20, 30]
    results = {num: num < 0 for num in numbers}
    return results

if __name__ == '__main__':
    print(check_negatives())