def get_ordered_pair(a, b):
    if a < b:
        return a, b
    return b, a

if __name__ == '__main__':
    result = get_ordered_pair(5, 2)
    print(result)