def is_odd(num):
    return num % 2 != 0

if __name__ == '__main__':
    test_values = {'seventeen': 17, 'forty-two': 42, 'negative three': -3, 'zero': 0}
    for name, value in test_values.items():
        print(f"Is {value} (named '{name}') odd? {is_odd(value)}")