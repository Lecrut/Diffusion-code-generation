def get_larger_value(m1, m2):
    if m1 >= m2:
        return m1
    else:
        return m2

if __name__ == '__main__':
    result = get_larger_value(1.5, 2.0)
    print(result)