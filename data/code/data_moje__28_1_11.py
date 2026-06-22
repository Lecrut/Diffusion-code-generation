def sort_descending(a, b):
    if a > b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    val_a = 10
    val_b = 5
    result = sort_descending(val_a, val_b)
    print(result)