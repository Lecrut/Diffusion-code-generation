def find_max(values):
    if not values:
        return None
    max_val = values[0]
    for num in values:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    data = [3.14, 2.71, 9.86, 1.41, 5.67]
    print(find_max(data))