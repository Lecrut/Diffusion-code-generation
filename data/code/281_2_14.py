SUM_CONSTANTS = {
    'a': 10,
    'b': 25,
    'c': 30,
    'd': 5,
    'e': 45
}

def sum_five_integers(a, b, c, d, e):
    total = 0
    for value in [a, b, c, d, e]:
        total += value
    return total

if __name__ == '__main__':
    result = sum_five_integers(**SUM_CONSTANTS)
    print(result)