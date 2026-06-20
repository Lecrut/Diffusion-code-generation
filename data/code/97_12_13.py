INPUT_VAR1 = 'x'
INPUT_VAR2 = 'y'
VALUES = [0, 1]

def xor_table():
    results = []
    for x in VALUES:
        for y in VALUES:
            result = x != y
            results.append((x, y, int(result)))
    print(f'{'X':<5} {'Y':<5} {'Result':<10}')
    for row in results:
        print(f'{row[0]:<5} {row[1]:<5} {row[2]:<10}')
if __name__ == '__main__':
    xor_table()