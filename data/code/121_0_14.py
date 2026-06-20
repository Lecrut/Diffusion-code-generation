def compare_values(a, b):
    return a if a > b else b

if __name__ == '__main__':
    print(compare_values(10**18, 2**64))