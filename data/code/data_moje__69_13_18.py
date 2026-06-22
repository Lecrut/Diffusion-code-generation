CONVERSION_FACTOR = 5280

def m_to_f(miles):
    return miles * CONVERSION_FACTOR

if __name__ == '__main__':
    test_cases = [0, 2.5, 100]
    for val in test_cases:
        print(m_to_f(val))