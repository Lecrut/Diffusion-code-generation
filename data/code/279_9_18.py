if __name__ == '__main__':
    multiples = {3: 'Fizz', 5: 'Buzz'}
    for i in range(1, 101):
        output = ''.join(multiples[k] for k in multiples if i % k == 0)
        print(output or i)