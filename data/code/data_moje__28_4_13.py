def sort_reverse(a, b):
    return sorted([a, b], reverse=True)

if __name__ == '__main__':
    result = sort_reverse(10, 5)
    print(result)