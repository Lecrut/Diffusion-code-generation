def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    result = get_penultimate([10, 20, 30, 40])
    print(result)