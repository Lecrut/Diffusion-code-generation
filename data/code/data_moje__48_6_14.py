import operator

def find_max_integers(integers):
    return max(integers, key=operator.identity)

if __name__ == '__main__':
    values = [10, 25, 3, 99, 42, 7]
    result = find_max_integers(values)
    print(result)