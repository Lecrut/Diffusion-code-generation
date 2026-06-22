TARGET_NUMBER = 6
MIN_MULTIPLIER = 1
MAX_MULTIPLIER = 10

def build_table(n):
    return dict((k, n * k) for k in range(MIN_MULTIPLIER, MAX_MULTIPLIER + 1))

if __name__ == '__main__':
    table = build_table(TARGET_NUMBER)
    print(table)