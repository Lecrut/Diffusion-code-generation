def sort_descending(a, b):
    if a > b:
        return a, b
    return b, a

if __name__ == '__main__':
    result = sort_descending(10, 25)
    print(result)