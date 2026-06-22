def sort_pair(a, b):
    if a > b:
        return [b, a]
    return [a, b]

if __name__ == '__main__':
    result = sort_pair(5, 3)
    print(result)