def sort_descending(a, b):
    return sorted([a, b], reverse=True)

if __name__ == '__main__':
    result = sort_descending(10, 5)
    print(result)