import functools

def compare_elements(lst):
    return lst[0] > lst[5]

if __name__ == '__main__':
    sample = [100, 20, 30, 40, 50, 60]
    print(compare_elements(sample))