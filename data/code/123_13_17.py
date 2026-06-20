MAX_NUMBER = 100

def sum_range():
    return sum(x for x in range(1, MAX_NUMBER + 1))

if __name__ == '__main__':
    result = sum_range()
    print(result)