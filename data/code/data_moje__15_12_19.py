def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    sample = [10, 20, 30, 40, 50]
    print(get_penultimate(sample))