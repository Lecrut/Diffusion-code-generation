a = 10
b = 5

def sort_descending(x, y):
    if x >= y:
        return [x, y]
    else:
        return [y, x]

if __name__ == '__main__':
    result = sort_descending(a, b)
    print(result)