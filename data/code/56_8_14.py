TARGET_NUMBER = 6
MULTIPLIER_RANGE = range(1, 11)

def build_table_for(number, multipliers):
    result = {}
    for m in multipliers:
        product = number * m
        result[m] = product
    return result

if __name__ == '__main__':
    multipliers = MULTIPLIER_RANGE
    table = build_table_for(TARGET_NUMBER, multipliers)
    print(table)