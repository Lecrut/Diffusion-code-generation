def is_odd(num):
    return num & 1 == 1

if __name__ == '__main__':
    sample_values = [5, 8, 21, 4]
    results = {num: is_odd(num) for num in sample_values}
    print(results)