def sort_descending(a, b):
    if a < b:
        return [b, a]
    return [a, b]

if __name__ == '__main__':
    result = sort_descending(10, 20)
    print(result)