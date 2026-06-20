def is_odd(n):
    return n & 1

if __name__ == '__main__':
    sample_values = [2, 3, 5, 8, 10, 13]
    results = {num: is_odd(num) for num in sample_values}
    print(results)