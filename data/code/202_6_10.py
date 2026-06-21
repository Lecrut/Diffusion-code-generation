MAX_VALUE = float('-inf')

def find_largest(data):
    global MAX_VALUE
    if data:
        for item in data:
            if item > MAX_VALUE:
                MAX_VALUE = item

if __name__ == '__main__':
    sample_series = [15, 8, 42, 3, 99, 22]
    find_largest(sample_series)
    print(MAX_VALUE)